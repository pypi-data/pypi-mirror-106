__version__ = "0.0.0"


from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
    Iterable,
    Tuple,
)


WSGIApp_t = Callable[
    [Dict[str, Any], Callable[[Iterable[Tuple[str, str]]], None]],
    Iterable[bytes],
]
ASGIApp_t = Callable[
    [
        Dict[str, Any],
        Callable[[], Awaitable[Dict[str, Any]]],
        Callable[[Dict[str, Any]], Awaitable[None]]
    ],
    Awaitable[None]
]
