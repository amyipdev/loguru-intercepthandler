#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later

# Code derived from the README on github:Delgan/loguru,
# which uses the MIT license.

import inspect
import logging

from loguru import logger

class _InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        level: str | int
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        f, d = inspect.currentframe(), 0
        while f and (d == 0 or f.f_code.co_filename == logging.__file__):
            f = f.f_back
            d += 1
        logger.opt(depth=d, exception=record.exc_info).log(level, record.getMessage())

def setup():
    logging.basicConfig(handlers=[_InterceptHandler()], level=0, force=True)
