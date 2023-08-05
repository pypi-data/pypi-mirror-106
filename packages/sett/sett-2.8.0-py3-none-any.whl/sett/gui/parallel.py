import logging
import sys
import traceback
from typing import Sequence, Callable, Optional, cast
from contextlib import contextmanager

from .pyside import QtCore
from ..utils.log import LOG_FORMAT
from ..utils.error_handling import (
    suppress_exceptions,
    log_exceptions,
    error_report_on_exception,
)
from ..utils.config import Config
from ..core.secret import enforce_secret_by_signature

from .. import RUNTIME_INFO


class LoggerHandler(logging.Handler):
    def __init__(self, level=logging.NOTSET, callback=None):
        super().__init__(level)
        self.callback = callback

    def emit(self, record):
        if self.callback:
            self.callback(self.format(record))


class WorkerSignals(QtCore.QObject):
    started = QtCore.Signal()
    finished = QtCore.Signal()
    error = QtCore.Signal(tuple)
    result = QtCore.Signal(object)
    progress = QtCore.Signal(int)
    logging = QtCore.Signal(str)


class Worker(QtCore.QRunnable):
    """Worker can run an arbitrary function in a separate thread.

    :param fn: function to run in a thread
    :param args: arguments passed to the function
    :param kwargs: keyword arguments passed to the function
    :param logger: logs from those loggers are passed to the logging
                   signal
    """

    def __init__(
        self,
        fn,
        *args,
        capture_loggers: Sequence[logging.Logger] = (),
        ignore_exceptions: bool = False,
        forward_errors: Optional[Callable[[str], None]] = None,
        report_config: Config,
        **kwargs,
    ):
        super().__init__()
        logger = (
            capture_loggers[0] if capture_loggers else cast(logging.Logger, logging)
        )
        # Somehow pyling does not know, that @contextmanager also is a decorator:
        sanitized_args, sanitized_kwargs = enforce_secret_by_signature(fn, args, kwargs)
        workflow_args_info = ",\n  ".join(
            [repr(arg) for arg in sanitized_args]
            + [f"{key}={repr(val)}" for key, val in sanitized_kwargs.items()]
        )
        self.fn = log_exceptions(logger=logger)(fn)
        if report_config.error_reports:
            self.fn = error_report_on_exception(  # pylint: disable=not-callable
                report_config,
                context=f"{fn.__name__}({workflow_args_info})",
            )(fn)
        if ignore_exceptions:
            self.fn = suppress_exceptions(self.fn)
        self.args = args
        self.kwargs = kwargs
        self.capture_loggers = capture_loggers
        self.signals = WorkerSignals()  # progress signal is not implemented
        if forward_errors is not None:
            self.signals.error.connect(lambda err: forward_errors(err[1]))

    def run(self) -> None:
        with attach_loggers_to_signals(self.capture_loggers, self.signals):
            try:
                self.signals.started.emit()
                self.signals.logging.emit(RUNTIME_INFO)
                result = self.fn(*self.args, **self.kwargs)
            except Exception:  # pylint: disable=broad-except
                exctype, value, _ = sys.exc_info()
                self.signals.error.emit((exctype, value, traceback.format_exc()))
            else:
                self.signals.result.emit(result)
        self.signals.finished.emit()


@contextmanager
def attach_loggers_to_signals(loggers, signals):
    logger_handler = LoggerHandler(callback=signals.logging.emit)
    logger_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger_handler.setLevel(logging.INFO)
    for logger in loggers:
        logger.addHandler(logger_handler)
    yield None
    for logger in loggers:
        logger.removeHandler(logger_handler)
