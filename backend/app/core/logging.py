"""Logging utilities for the FastAPI application."""
from __future__ import annotations

import logging
from logging.config import dictConfig


def setup_logging(*, level: str | int = "INFO") -> None:
    """Configure application-wide logging."""

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "()": "uvicorn.logging.DefaultFormatter",
                    "fmt": "%(levelprefix)s [%(name)s] %(message)s",
                    "use_colors": True,
                }
            },
            "handlers": {
                "default": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                }
            },
            "loggers": {
                "uvicorn": {"handlers": ["default"], "level": level},
                "uvicorn.error": {"handlers": ["default"], "level": level, "propagate": False},
                "uvicorn.access": {"handlers": ["default"], "level": level, "propagate": False},
                "app": {"handlers": ["default"], "level": level, "propagate": False},
            },
        }
    )

    logging.getLogger("app").debug("Logging configured with level %s", level)
