import ssl
import typing as t

from gileum import BaseGileum
import gunicorn.glogging
from gunicorn.app.base import BaseApplication
from gunicorn.arbiter import Arbiter
from gunicorn.http.message import Request
from gunicorn.http.wsgi import Response
from gunicorn.workers.base import Worker

from . import WSGIApp_t
from .types import Literal


HookArbiter_t = t.Callable[[Arbiter], None]
HookWorker_t = t.Callable[[Worker], None]
HookArbiterWorker_t = t.Callable[[Arbiter, Worker], None]
HookPreRequest_t = t.Callable[[Worker, Request], None]
HookPostRequest_t = t.Callable[[Worker, Request, t.Dict[str, t.Any], Response], None]
HookNworkersChanged_t = t.Callable[[Arbiter, int, int], None]


class GunicornGileum(BaseGileum):

    # Reference at https://docs.gunicorn.org/en/latest/settings.html

    # Debugging
    reload: bool = False
    reload_engine: Literal["auto", "poll", "inotify"] = "auto"
    reload_extra_files: t.List[str] = []
    spew: bool = False
    check_config: bool = False
    print_config: bool = False

    # Logging
    accesslog: t.Optional[str] = None
    disable_redirect_access_to_syslog: bool = False
    access_log_format: t.Optional[str] = None
    errorlog: str = "-"
    loglevel: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"
    capture_output: bool = False
    logger_class: t.Any = gunicorn.glogging.Logger
    logconfig: t.Optional[str] = None
    logconfig_dict: dict = {}
    syslog_addr: str = "udp://localhost:514"
    syslog: bool = False
    syslog_prefix: t.Optional[str] = None
    syslog_facility: str = "user"
    enable_stdio_inheritance: bool = False
    statsd_host: t.Optional[str] = None
    dogstatsd_tags: str = ""
    statsd_prefix: str = ""

    # Process Naming
    proc_name: t.Optional[str] = None
    default_proc_name: str = "gunicorn"

    # SSL
    keyfile: t.Optional[str] = None
    certfile: t.Optional[str] = None
    ssl_version: ssl._SSLMethod = ssl.PROTOCOL_SSLv23
    cert_reqs: ssl.VerifyMode = ssl.VerifyMode.CERT_NONE
    ca_certs: t.Optional[str] = None
    suppress_ragged_eofs: bool = True
    do_handshake_on_connect: bool = False
    ciphers: t.Optional[str] = None

    # Security
    limit_request_line: int = 4094
    limit_request_fields: int = 100
    limit_request_field_size: int = 8190

    # Server Hooks
    on_starting: t.Optional[HookArbiter_t] = None
    on_reload: t.Optional[HookArbiter_t] = None
    when_ready: t.Optional[HookArbiter_t] = None
    pre_fork: t.Optional[HookArbiterWorker_t] = None
    post_fork: t.Optional[HookArbiterWorker_t] = None
    post_worker_init: t.Optional[HookWorker_t] = None
    worker_init: t.Optional[HookWorker_t] = None
    worker_int: t.Optional[HookWorker_t] = None
    worker_abort: t.Optional[HookWorker_t] = None
    pre_exec: t.Optional[HookArbiter_t] = None
    pre_request: t.Optional[HookPreRequest_t] = None
    post_request: t.Optional[HookPostRequest_t] = None
    child_exit: t.Optional[HookArbiterWorker_t] = None
    worker_exit: t.Optional[HookArbiterWorker_t] = None
    nworkers_changed: t.Optional[HookNworkersChanged_t] = None
    on_exit: t.Optional[HookArbiter_t] = None

    # ServerMechanics
    preload_app: bool = False
    sendfile: t.Optional[str] = None
    reuse_port: bool = False
    chdir: t.Optional[str] = None
    daemon: bool = False
    raw_env: t.List[str] = []
    pidfile: t.Optional[str] = None
    worker_tmp_dir: t.Optional[str] = None
    user: t.Optional[int] = None
    group: t.Optional[int] = None
    umask: int = 0
    initgroups: bool = False
    tmp_upload_dir: t.Optional[str] = None
    secure_scheme_headers: t.Optional[t.Dict[str, str]] = None
    forwarded_allow_ips: str = "127.0.0.1"
    pythonpath: t.Optional[str] = None
    paste: t.Optional[str] = None
    proxy_protocol: bool = False
    proxy_allow_ips: str = "127.0.0.1"
    raw_paste_global_conf: t.List[str] = []
    strip_header_spaces: bool = False

    # Server Socket
    bind: t.List[str] = ["127.0.0.1:8000"]
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

    def __init__(self, app, options: t.Dict[str, t.Any] = None):
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


GunicornServer_t = t.TypeVar("GunicornServer_t", bound=GunicornServer)



def run_gunicorn(
    app: WSGIApp_t,
    glm: GunicornGileum,
    server: t.Type[GunicornServer_t] = GunicornServer,
) -> None:
    server(app, glm.dict(exclude={"glm_name"})).run()
