from __future__ import annotations

import logging
import sys

from rich.console import Console


def get_logger(verbose: bool = False) -> logging.Logger:
    logger = logging.getLogger("paios")
    if logger.handlers:
        return logger

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("[%(levelname)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    return logger


console: Console | None = None


def get_console() -> Console:
    global console
    if console is None:
        console = Console()
    return console
