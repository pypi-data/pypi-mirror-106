import ssl
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Type,
    TypeVar,
)

from gileum import BaseGileum
import gunicorn.glogging
from gunicorn.app.base import BaseApplication
from gunicorn.arbiter import Arbiter
from gunicorn.http.message import Request
from gunicorn.http.wsgi import Response
from gunicorn.workers.base import Worker

from . import WSGIApp_t


HookArbiter_t = Callable[[Arbiter], None]
HookWorker_t = Callable[[Worker], None]
HookArbiterWorker_t = Callable[[Arbiter, Worker], None]
HookPreRequest_t = Callable[[Worker, Request], None]
HookPostRequest_t = Callable[[Worker, Request, Dict[str, Any], Response], None]
HookNworkersChanged_t = Callable[[Arbiter, int, int], None]


class GunicornGileum(BaseGileum):

    glm_name: Literal["main"] = "main"

    # Reference at https://docs.gunicorn.org/en/latest/settings.html

    # NOTE
    #   Remove this parameter beacause a gunicorn server should be launched
    #   by calling `run_server` function.
    #
    # wsgi_app: Optional[str] = None

    # Debugging
    reload: bool = False
    reload_engine: Literal["auto", "poll", "inotify"] = "auto"
    reload_extra_files: List[str] = []
    spew: bool = False
    check_config: bool = False
    print_config: bool = False

    # Logging
    accesslog: Optional[str] = None
    disable_redirect_access_to_syslog: bool = False
    access_log_format: Optional[str] = None
    errorlog: str = "-"
    loglevel: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"
    capture_output: bool = False
    logger_class: Any = gunicorn.glogging.Logger
    logconfig: Optional[str] = None
    logconfig_dict: dict = {}
    syslog_addr: str = "udp://localhost:514"
    syslog: bool = False
    syslog_prefix: Optional[str] = None
    syslog_facility: str = "user"
    enable_stdio_inheritance: bool = False
    statsd_host: Optional[str] = None
    dogstatsd_tags: str = ""
    statsd_prefix: str = ""

    # Process Naming
    proc_name: Optional[str] = None
    default_proc_name: str = "gunicorn"

    # SSL
    keyfile: Optional[str] = None
    certfile: Optional[str] = None
    ssl_version: ssl._SSLMethod = ssl.PROTOCOL_SSLv23
    cert_reqs: ssl.VerifyMode = ssl.VerifyMode.CERT_NONE
    ca_certs: Optional[str] = None
    suppress_ragged_eofs: bool = True
    do_handshake_on_connect: bool = False
    ciphers: Optional[str] = None

    # Security
    limit_request_line: int = 4094
    limit_request_fields: int = 100
    limit_request_field_size: int = 8190

    # Server Hooks
    on_starting: Optional[HookArbiter_t] = None
    on_reload: Optional[HookArbiter_t] = None
    when_ready: Optional[HookArbiter_t] = None
    pre_fork: Optional[HookArbiterWorker_t] = None
    post_fork: Optional[HookArbiterWorker_t] = None
    post_worker_init: Optional[HookWorker_t] = None
    worker_init: Optional[HookWorker_t] = None
    worker_int: Optional[HookWorker_t] = None
    worker_abort: Optional[HookWorker_t] = None
    pre_exec: Optional[HookArbiter_t] = None
    pre_request: Optional[HookPreRequest_t] = None
    post_request: Optional[HookPostRequest_t] = None
    child_exit: Optional[HookArbiterWorker_t] = None
    worker_exit: Optional[HookArbiterWorker_t] = None
    nworkers_changed: Optional[HookNworkersChanged_t] = None
    on_exit: Optional[HookArbiter_t] = None

    # ServerMechanics
    preload_app: bool = False
    sendfile: Optional[str] = None
    reuse_port: bool = False
    chdir: Optional[str] = None
    daemon: bool = False
    raw_env: List[str] = []
    pidfile: Optional[str] = None
    worker_tmp_dir: Optional[str] = None
    user: Optional[int] = None
    group: Optional[int] = None
    umask: int = 0
    initgroups: bool = False
    tmp_upload_dir: Optional[str] = None
    secure_scheme_headers: Optional[Dict[str, str]] = None
    forwarded_allow_ips: str = "127.0.0.1"
    pythonpath: Optional[str] = None
    paste: Optional[str] = None
    proxy_protocol: bool = False
    proxy_allow_ips: str = "127.0.0.1"
    raw_paste_global_conf: List[str] = []
    strip_header_spaces: bool = False

    # Server Socket
    bind: List[str] = ["127.0.0.1:8000"]
    backlog: int = 2048

    # Worker Processes
    workers: int = 1
    worker_class: Literal[
        "sync",
        "eventlet",
        "gevent",
        "tornado",
        "gthread"
    ] = "sync"
    threads: int = 1
    worker_connections: int = 1000
    max_requests: int = 0
    max_requests_jitter: int = 0
    timeout: int = 30
    graceful_timeout: int = 30
    keepalive: int = 2


class GunicornServer(BaseApplication):

    # Reference at https://docs.gunicorn.org/en/latest/custom.html

    def __init__(self, app, options: Dict[str, Any] = None):
        self.options = options or {}
        self.app = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.app


GunicornServer_t = TypeVar("GunicornServer_t", bound=GunicornServer)



def run_gunicorn(
    app: WSGIApp_t,
    glm: GunicornGileum,
    server: Type[GunicornServer_t] = GunicornServer,
) -> None:
    server(app, glm.dict(exclude={"glm_name"})).run()
