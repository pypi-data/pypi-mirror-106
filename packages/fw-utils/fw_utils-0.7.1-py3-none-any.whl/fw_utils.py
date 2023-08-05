"""Flywheel utilities and common helpers."""
import functools
import importlib.metadata as importlib_metadata
import os
import re
import threading
import time
import typing as t
from collections.abc import Callable
from pathlib import Path
from tempfile import SpooledTemporaryFile

__version__ = importlib_metadata.version(__name__)


# FORMATTERS


PLURALS = {
    "study": "studies",
    "series": "series",
    "analysis": "analyses",
}


def pluralize(singular: str, plural: str = "") -> str:
    """Return plural for given singular noun."""
    if plural:
        PLURALS[singular.lower()] = plural.lower()
    return PLURALS.get(singular, f"{singular}s")


def quantify(num: int, singular: str, plural: str = "") -> str:
    """Return "counted str" for given num and word: (3,'file') => '3 files'."""
    if num == 1:
        return f"1 {singular}"
    plural = pluralize(singular, plural)
    return f"{num} {plural}"


def hrsize(size: float) -> str:
    """Return human-readable file size for given number of bytes."""
    unit, decimals = "B", 0
    for unit in "BKMGTPEZY":
        decimals = 0 if unit == "B" or round(size) > 9 else 1
        if round(size) < 100 or unit == "Y":
            break
        size /= 1024.0
    return f"{size:.{decimals}f}{unit}"


def hrtime(seconds: float) -> str:
    """Return human-readable time duration for given number of seconds."""
    remainder = seconds
    parts: t.List[str] = []
    units = {"y": 31536000, "w": 604800, "d": 86400, "h": 3600, "m": 60, "s": 1}
    for unit, seconds_in_unit in units.items():
        quotient, remainder = divmod(remainder, seconds_in_unit)
        if len(parts) > 1 or (parts and not quotient):
            break
        if unit == "s" and not parts:
            decimals = 0 if round(quotient) >= 10 or not round(remainder, 1) else 1
            parts.append(f"{quotient + remainder:.{decimals}f}{unit}")
        elif quotient >= 1:
            parts.append(f"{int(quotient)}{unit}")
    return " ".join(parts)


class Timer:  # pylint: disable=too-few-public-methods
    """Timer for creating size/speed reports on file processing/transfers."""

    # pylint: disable=redefined-builtin
    def __init__(self, files: int = 0, bytes: int = 0) -> None:
        """Init timer w/ current timestamp and the no. of files/bytes."""
        self.start = time.time()
        self.files = files
        self.bytes = bytes

    def report(self) -> str:
        """Return message with size and speed info based on the elapsed time."""
        elapsed = time.time() - self.start
        size, speed = [], []
        if self.files or not self.bytes:
            size.append(quantify(self.files, "file"))
            speed.append(f"{self.files / elapsed:.1f}/s")
        if self.bytes:
            size.append(hrsize(self.bytes))
            speed.append(hrsize(self.bytes / elapsed) + "/s")
        return f"{'|'.join(size)} in {hrtime(elapsed)} [{'|'.join(speed)}]"


def str_to_python_id(raw_string: str) -> str:
    """Convert any string to a valid python identifier in a reversible way."""

    def char_to_hex(match: t.Match) -> str:
        return f"__{ord(match.group(0)):02x}__"

    raw_string = re.sub(r"^[^a-z_]", char_to_hex, raw_string, flags=re.I)
    return re.sub(r"[^a-z_0-9]{1}", char_to_hex, raw_string, flags=re.I)


def python_id_to_str(python_id: str) -> str:
    """Convert a python identifier back to the original/normal string."""

    def hex_to_char(match: t.Match) -> str:
        return chr(int(match.group(1), 16))

    return re.sub(r"__([a-f0-9]{2})__", hex_to_char, python_id)


# PARSERS


def parse_hrsize(value: str) -> float:
    """Return number of bytes for given human-readable file size."""
    pattern = r"(?P<num>\d+(\.\d*)?)\s*(?P<unit>([KMGTPEZY]i?)?B?)"
    match = re.match(pattern, value, flags=re.I)
    if match is None:
        raise ValueError(f"Cannot parse human-readable size: {value}")
    num = float(match.groupdict()["num"])
    unit = match.groupdict()["unit"].upper().rstrip("BI") or "B"
    units = {u: 1024 ** i for i, u in enumerate("BKMGTPEZY")}
    return num * units[unit]


def parse_hrtime(value: str) -> float:
    """Return number of seconds for given human-readable time duration."""
    parts = value.split()
    units = {"y": 31536000, "w": 604800, "d": 86400, "h": 3600, "m": 60, "s": 1}
    seconds = 0.0
    regex = re.compile(r"(?P<num>\d+(\.\d*)?)(?P<unit>[ywdhms])", flags=re.I)
    for part in parts:
        match = regex.match(part)
        if match is None:
            raise ValueError(f"Cannot parse human-readable time: {part}")
        num, unit = float(match.group("num")), match.group("unit").lower()
        seconds += num * units[unit]
    return seconds


URL_RE = re.compile(
    r"^"
    r"(?P<scheme>[^:]+)://"
    r"((?P<username>[^:]+):(?P<password>[^@]+)@)?"
    r"(?P<host>[^:/?#]*)"
    r"(:(?P<port>\d+))?"
    r"((?P<path>/[^?#]+))?"
    r"(\?(?P<query>[^#]+))?"
    r"(#(?P<fragment>.*))?"
    r"$"
)


def parse_url(url: str, pattern: t.Pattern = URL_RE) -> t.Dict[str, str]:
    """Return dictionary of fields parsed from a URL."""
    match = pattern.match(url)
    if not match:
        raise ValueError(f"Invalid URL: {url}")
    parsed = {k: v for k, v in match.groupdict().items() if v is not None}
    params = parsed.pop("query", "")
    if params:
        # store query params directly on the result
        for param in params.split("&"):
            if "=" not in param:
                param = f"{param}="
            key, value = param.split("=", maxsplit=1)
            if "," in value:
                value = value.split(",")
            parsed[key] = value
    return attrify(parsed)


# DICTS


class AttrDict(dict):
    """Dictionary with attribute access to valid-python-id keys."""

    def __getattr__(self, name: str):
        """Return dictionary keys as attributes."""
        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError(name) from exc


def attrify(data):
    """Return data with dicts cast to attrdict for dot notation access."""
    if isinstance(data, dict):
        return AttrDict((key, attrify(value)) for key, value in data.items())
    if isinstance(data, list):
        return [attrify(elem) for elem in data]
    return data


def flatten_dotdict(deep: dict, prefix: str = "") -> dict:
    """Flatten dictionary using dot-notation: {a: b: c} => {a.b: c}."""
    flat = {}
    for key, value in deep.items():
        key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            flat.update(flatten_dotdict(value, prefix=key))
        else:
            flat[key] = value
    return flat


def inflate_dotdict(flat: dict) -> dict:
    """Inflate flat dot-notation dictionary: {a.b: c} => {a: b: c}."""
    deep = node = {}  # type: ignore
    for key, value in flat.items():
        parts = key.split(".")
        path, key = parts[:-1], parts[-1]
        for part in path:
            node = node.setdefault(part, {})
        node[key] = value
        node = deep
    return deep


# FILES

SPOOLED_TMP_MAX_SIZE = 1 << 20  # 1MB

AnyPath = t.Union[str, Path]
AnyFile = t.Union[AnyPath, t.IO]


class BinFile:
    """File class for accessing local paths and file-like objects similarly."""

    def __init__(self, file: AnyFile, mode: str = "rb", metapath: str = "") -> None:
        """Open a file for reading or writing.

        Args:
            file (str|Path|file): The local path to open or a file-like object.
            mode (str, optional): The file opening mode, rb|wb. Default: rb.
            metapath (str, optional): Override metapath attribute if given.
        """
        if mode not in {"rb", "wb"}:
            raise ValueError(f"Invalid file mode: {mode} (expected rb|wb)")
        self.file: t.IO = None  # type: ignore
        self.file_open = False
        self.localpath = None
        self.mode = mode
        mode_func = "readable" if mode == "rb" else "writable"
        if isinstance(file, (str, Path)):
            self.file_open = True
            self.localpath = str(Path(file).resolve())
            file = Path(self.localpath).open(mode=mode)
        if not hasattr(file, mode_func) or not getattr(file, mode_func)():
            raise ValueError(f"File {file!r} is not {mode_func}")
        self.file = file
        self.metapath = metapath or self.localpath

    def __getattr__(self, name: str):
        """Return attrs proxied from the file."""
        return getattr(self.file, name)

    def __iter__(self):
        """Iterate over lines."""
        return self.file.__iter__()

    def __next__(self):
        """Get next line."""
        return self.file.__next__()

    def __enter__(self) -> "BinFile":
        """Enter 'with' context - seek to start if it's a BinaryIO or a TempFile."""
        self.file.seek(0)
        return self

    def __exit__(self, exc_cls, exc_val, exc_trace) -> None:
        """Exit 'with' context - close file if it was opened by BinFile."""
        if self.file_open:
            self.file.close()

    def __repr__(self) -> str:
        """Return string representation of the BinFile."""
        file_str = self.metapath or f"{type(self.file).__name__}/{hex(id(self.file))}"
        return f"{type(self).__name__}('{file_str}', mode='{self.mode}')"


def open_any(file: t.Union[AnyFile, BinFile], mode: str = "rb") -> BinFile:
    """Return BinFile object as-is or AnyFile loaded as BinFile."""
    if isinstance(file, BinFile):
        if mode != file.mode:
            raise ValueError(f"open_any {mode!r} on a {file.mode!r} BinFile")
        return file
    return BinFile(file, mode=mode)


def fileglob(
    dirpath: AnyPath,
    pattern: str = "*",
    recurse: bool = False,
) -> t.List[Path]:
    """Return the list of files under a given directory.

    Args:
        dirpath (str|Path): The directory path to glob in.
        pattern (str, optional): The glob pattern to match files on. Default: "*".
        recurse (bool, optional): Toggle for enabling recursion. Default: False.

    Returns:
        list[Path]: The file paths that matched the glob within the directory.
    """
    if isinstance(dirpath, str):
        dirpath = Path(dirpath)
    glob_fn = getattr(dirpath, "rglob" if recurse else "glob")
    return list(sorted(f for f in glob_fn(pattern) if f.is_file()))


class TempFile(SpooledTemporaryFile):
    """Extend SpooledTemporaryFile class with readable and writable methods."""

    _file: t.IO

    def __init__(self, max_size: int = SPOOLED_TMP_MAX_SIZE, dir: str = None):
        """Simplified interface to create a SpooledTemporaryFile instance."""
        # pylint: disable=redefined-builtin
        super().__init__(max_size=max_size, dir=dir)

    def readable(self) -> bool:
        """Return that the file is readable."""
        return self._file.readable()

    def writable(self) -> bool:
        """Return that the file is writable."""
        return self._file.writable()

    def seekable(self) -> bool:
        """Return that the file is seekable."""
        return self._file.seekable()


# CACHING


class Cached:
    """Descriptor for caching attributes and injecting dependencies."""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        init: t.Callable,
        args: t.Optional[t.List["Cached"]] = None,
        clear: t.Optional[t.Callable] = None,
        fork_safe: bool = False,
        thread_safe: bool = True,
    ) -> None:
        """Initialize the cached attribute descriptor.

        Args:
            init (callable): The function to init the attribute with on access.
            args (list[Cached]): List of cached attributes to load and pass to
                the init function as arguments for dependency injection.
            clear (callable): Optional callback to tear down the attribute with.
            fork_safe: (bool): Set to True to enable sharing between processes.
            thread_safe: (bool): Set to False disable sharing between threads.
        """
        self.init = init
        self.args = args or []
        self.clear = clear
        if fork_safe and not thread_safe:
            raise ValueError(  # pragma: no cover
                "Thread IDs are only unique within a single process. Using "
                "fork_safe=True and thread_safe=False is not allowed."
            )
        self.fork_safe = fork_safe
        self.thread_safe = thread_safe
        self.name = ""

    def __set_name__(self, owner: type, name: str) -> None:
        """Store the descriptor attribute name as defined on the owner class."""
        self.name = name

    def __get__(self, instance, owner: t.Optional[type] = None):
        """Return the initialized attribute (cached)."""
        # accessed as a class attribute - return the descriptor
        if instance is None:
            return self
        # accessed as an instance attribute - return the attribute
        cache = self.get_cache_dict(instance)
        key = self.get_cache_key()
        # initialize the attribute if it's not cached yet
        if key not in cache:
            # dependency injection - pass other cached attrs as args
            args = [arg.__get__(instance, owner) for arg in self.args]
            cache[key] = self.init(*args)
        return cache[key]

    def __set__(self, instance, value) -> None:
        """Set arbitrary attribute value."""
        cache = self.get_cache_dict(instance)
        key = self.get_cache_key()
        cache[key] = value

    def __delete__(self, instance) -> None:
        """Delete the cached attribute."""
        cache = self.get_cache_dict(instance)
        key = self.get_cache_key()
        # tear down the attribute if it's cached
        if key in cache:
            if self.clear:
                self.clear(cache[key])
            # remove from the cache dict and call an explicit del on the attr
            del cache[key]
            del key

    @staticmethod
    def get_cache_dict(instance) -> dict:
        """Return the cache dict of the given instance."""
        return instance.__dict__.setdefault("_cached", {})

    def get_cache_key(self) -> str:
        """Return the cache key based on multiprocess/thread safety."""
        key = f"/{self.name}"
        if not self.fork_safe:
            key = f"{key}/pid:{os.getpid()}"
        if not self.thread_safe:
            key = f"{key}/tid:{threading.get_ident()}"
        return key


# TEMPLATING


class Tokenizer:
    """Simple tokenizer to help parsing patterns."""

    def __init__(self, string: str):
        """Tokenize the given string."""
        self.string = string
        self.index = 0
        self.char: t.Optional[str] = None

    def __iter__(self) -> "Tokenizer":
        """Return tokenizer itself as an iterator."""
        return self

    def __next__(self) -> str:
        """Get the next char or 2 chars if it's escaped."""
        index = self.index
        try:
            char = self.string[index]
        except IndexError as exc:
            raise StopIteration from exc

        if char == "\\":
            index += 1
            try:
                char += self.string[index]
            except IndexError as exc:
                raise ValueError("Pattern ending with backslash") from exc

        self.index = index + 1
        self.char = char
        return char

    def get_until(self, terminals: t.Optional[str] = None) -> str:
        """Get until terminal character or until the end if no terminals specified."""
        result = ""
        for char in self:
            if terminals and char in terminals:
                break
            result += char
        else:
            if terminals:
                raise ValueError(f"missing {terminals}, unterminated pattern")
        return result


# ASSERTING


@functools.singledispatch
def assert_like(  # pylint: disable=unused-argument
    expected, got, allow_extra=True, loc=""
) -> None:
    """Check whether an object is like the expected.

    Supported values:
    * dict: see 'assert_like_dict'
    * list: see 'assert_like_list'
    * regex pattern: see 'assert_like_pattern'
    * callable: see 'assert_like_function'
    * everything else: simply compared using '=='
    """
    assert expected == got, f"{loc}: {got} != {expected}"


@assert_like.register
def assert_like_dict(expected: dict, got, allow_extra=True, loc="") -> None:
    """Check whether a dictionary is like the expected.

    'allow_extra': enable extra keys in the dictionary or not
    """
    expected_keys = set(expected)
    got_keys = set(got)
    missing_keys = expected_keys - got_keys
    assert not missing_keys, f"{loc}: {missing_keys=}"
    if not allow_extra:
        extra_keys = got_keys - expected_keys
        assert not extra_keys, f"{loc}: {extra_keys=}"
    for key, value in sorted(expected.items()):
        assert_like(value, got[key], allow_extra=allow_extra, loc=f"{loc}.{key}")


@assert_like.register
def assert_like_list(expected: list, got, loc="", **kwargs) -> None:
    """Check whether a list is like the expected.

    Ellipsis can be used for partial matching ([..., 2] == [1, 2]).
    """
    assert isinstance(got, list), f"{loc} {got.__class__.__name__} != list"
    got_iter = iter(got)
    ellipsis = False
    for index, value in enumerate(expected):
        loc_ = f"{loc}[{index}]"
        if value is Ellipsis:
            ellipsis = True
            continue
        for got_ in got_iter:
            try:
                assert_like(value, got_, loc=loc_, **kwargs)
            except AssertionError:
                if not ellipsis:
                    raise
            else:
                ellipsis = False
                break
        else:
            raise AssertionError(f"{loc_}: unexpected end of list")
    if not ellipsis and (extra_items := list(got_iter)):
        raise AssertionError(f"{loc}: unexpected items: {extra_items=}")


@assert_like.register
def assert_like_pattern(expected: re.Pattern, got, loc="", **_) -> None:
    """Check whether a string matches the given pattern."""
    assert expected.search(got), f"{loc}: {got} !~ {expected.pattern}"


@assert_like.register
def assert_like_function(expected: Callable, got, loc="", **_) -> None:
    """Check whether an object is the expected using the callback function."""
    try:
        assert expected(got)
    except Exception as exc:
        ctx = None if isinstance(exc, AssertionError) else exc
        raise AssertionError(f"{loc}: {got} validation failed ({exc})") from ctx
