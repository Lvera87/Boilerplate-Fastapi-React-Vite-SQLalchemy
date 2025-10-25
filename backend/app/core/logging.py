"""Logging utilities for the FastAPI application."""
from __future__ import annotations

import logging
import logging.handlers
from logging.config import dictConfig
from pathlib import Path

from app.core.config import get_settings


def setup_logging(*, level: str | int = None) -> None:
    """Configure application-wide logging with file and console handlers."""
    if level is None:
        settings = get_settings()
        level = settings.log_level or "INFO"

    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "()": "uvicorn.logging.DefaultFormatter",
                    "fmt": "%(levelprefix)s [%(name)s] %(message)s",
                    "use_colors": True,
                },
                "detailed": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },
            "handlers": {
                "default": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                },
                "file": {
                    "formatter": "detailed",
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": "logs/app.log",
                    "maxBytes": 10485760,  # 10MB
                    "backupCount": 5,
                },
            },
            "loggers": {
                "uvicorn": {"handlers": ["default", "file"], "level": level},
                "uvicorn.error": {"handlers": ["default", "file"], "level": level, "propagate": False},
                "uvicorn.access": {"handlers": ["default"], "level": "INFO", "propagate": False},
                "app": {"handlers": ["default", "file"], "level": level, "propagate": False},
            },
        }
    )

    logging.getLogger("app").debug("Logging configured with level %s", level)
