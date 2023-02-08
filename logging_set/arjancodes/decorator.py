import logging
from functools import partial, wraps
from logging import FileHandler, StreamHandler
from typing import Optional


def with_logging(f, logger: logging.Logger):
    @wraps(f)
    def inner(*args, **kwargs):
        logger.info(f"Starting {f.__qualname__} function.")
        val = f(*args, **kwargs)
        logger.info(f"Finished {f.__qualname__} function.")
        return val

    return inner


class LoggerBuilder:
    def __init__(self, logger: Optional[logging.Logger] = None):
        self._logger = logger if logger else logging.getLogger()

    def set_level(self, level=logging.DEBUG):
        self._logger.setLevel(level=level)
        return self

    def add_handler(
        self,
        handler: logging.Handler,
        fmt: str = "%(asctime)s-%(levelname)s-%(message)s",
    ):
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

        return self

    def build(self) -> logging.Logger:
        return self._logger


level = logging.INFO

handler = FileHandler("basic.log")
handler_formatter = "%(asctime)s-%(levelname)s-%(message)s"

logger_builder = (
    LoggerBuilder().set_level(level).add_handler(handler, handler_formatter)
)

logger = logger_builder.build()
with_default_logging = partial(with_logging, logger=logger)


@with_default_logging
def main() -> int:
    return 10


if __name__ == "__main__":
    main()
