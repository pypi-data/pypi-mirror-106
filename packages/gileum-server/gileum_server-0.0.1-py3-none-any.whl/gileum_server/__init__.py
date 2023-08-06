__version__ = "0.0.1"


import typing as t


WSGIApp_t = t.Callable[
    [t.Dict[str, t.Any], t.Callable[[t.Iterable[t.Tuple[str, str]]], None]],
    t.Iterable[bytes],
]
ASGIApp_t = t.Callable[
    [
        t.Dict[str, t.Any],
        t.Callable[[], t.Awaitable[t.Dict[str, t.Any]]],
        t.Callable[[t.Dict[str, t.Any]], t.Awaitable[None]]
    ],
    t.Awaitable[None]
]
