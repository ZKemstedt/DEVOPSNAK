import logging
import sys
from pathlib import Path
from logging import handlers, Logger, Formatter

import coloredlogs

TRACE_LEVEL = logging.TRACE = 5
logging.addLevelName(TRACE_LEVEL, 'TRACE')


def monkeypatch_trace(self: Logger, msg: str, *args, **kwargs) -> None:
    """Log `msg` with severity `TRACE`."""
    if self.isEnabledFor(TRACE_LEVEL):
        self._log(TRACE_LEVEL, msg, args, **kwargs)


Logger.trace = monkeypatch_trace

if len(sys.argv) >= 2:
    try:
        log_level = sys.argv[2]
    except Exception:
        print(f'Error: invalid log level {sys.argv[2]}')
        sys.exit(1)
else:
    log_level = logging.INFO

format_string = '%(asctime)s | %(name)30s | %(levelname)8s | %(message)s'
log_format = Formatter(format_string)

log_file = Path('logs', 'client.log')
log_file.parent.mkdir(exist_ok=True)
file_handler = handlers.RotatingFileHandler(log_file, maxBytes=5242880, backupCount=5, encoding='utf8')
file_handler.setFormatter(log_format)

root_log = logging.getLogger()
root_log.setLevel(log_level)
root_log.addHandler(file_handler)

coloredlogs.DEFAULT_LEVEL_STYLES = {
    **coloredlogs.DEFAULT_LEVEL_STYLES,
    'trace': {'color': 246},
    'critical': {'background': 'red'},
    'debug': coloredlogs.DEFAULT_LEVEL_STYLES['info']
    }
coloredlogs.DEFAULT_LOG_LEVEL = log_level
coloredlogs.DEFAULT_LOG_FORMAT = format_string

coloredlogs.install(logger=root_log, stream=sys.stdout)
