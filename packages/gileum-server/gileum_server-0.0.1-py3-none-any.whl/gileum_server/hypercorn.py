import asyncio
import logging
import signal
import ssl
import typing as t

from gileum import BaseGileum
from hypercorn.asyncio import serve
from hypercorn.config import Config

from . import ASGIApp_t
from .types import (
    Literal,
    Logger_t,
    LoggerClass_t,
)


# Units
BYTES = 1
OCTETS = 1
SECONDS = 1.0


class HypercornGileum(BaseGileum):

    glm_name: Literal["main"] = "main"

    access_log_format: str =\
        '%(h)s %(l)s %(l)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
    accesslog: t.Union[Logger_t, str, None] = None
    alpn_protocols: t.List[str] = ["h2", "http/1.1"]
    alt_svc_headers: t.List[str] = []
    backlog: int = 100
    bind: t.Union[str, t.List[str]] = ["127.0.0.1:8000"]
    ca_certs: t.Optional[str] = None
    certfile: t.Optional[str] = None
    ciphers: str = "ECDHE+AESGCM"
    debug: bool = False
    dogstatsd_tags: str = ""
    errorlog: t.Union[Logger_t, str, None] = "-"
    graceful_timeout: float = 3 * SECONDS
    group: t.Optional[int] = None
    h11_max_incomplete_size: int = 16 * 1024 * BYTES
    h2_max_concurrent_streams: int = 100
    h2_max_header_list_size: int = 2 ** 16
    h2_max_inbound_frame_size: int = 2 ** 14 * OCTETS
    include_server_header: bool = True
    insecure_bind: t.Union[str, t.List[str]] = []
    keep_alive_timeout: float = 5 * SECONDS
    keyfile: t.Optional[str] = None
    logconfig: t.Optional[str] = None
    logconfig_dict: t.Optional[dict] = None
    logger_class: LoggerClass_t = logging.Logger
    loglevel: str = "INFO"
    max_app_queue_size: int = 10
    quic_bind: t.Union[str, t.List[str]] = []
    pid_path: t.Optional[str] = None
    root_path: str = ""
    server_names: t.List[str] = []
    shutdown_timeout: float = 60 * SECONDS
    ssl_handshake_timeout: float = 60 * SECONDS
    startup_timeout: float = 60 * SECONDS
    statsd_host: t.Optional[str] = None
    statsd_prefix: str = ""
    umask: t.Optional[int] = None
    use_reloader: bool = False
    user: t.Optional[int] = None
    verify_flags: t.Optional[ssl.VerifyFlags] = None
    verify_mode: t.Optional[ssl.VerifyMode] = None
    websocket_max_message_size: int = 16 * 1024 * 1024 * BYTES
    websocket_ping_interval: t.Optional[float] = None
    worker_class: str = "asyncio"
    workers: int = 1


_shutdown_event = asyncio.Event()


def _signal_hadler(*args: t.Any) -> None:
    _shutdown_event.set()


def run_hypercorn(app: ASGIApp_t, glm: HypercornGileum) -> None:
    config = Config.from_mapping(glm.dict(exclude={"glm_name"}))

    # TODO
    #   It's worth re-considering its signal handling.
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGTERM, _signal_hadler)
    loop.run_until_complete(
        serve(app, config, shutdown_trigger=_shutdown_event.wait)
    )
