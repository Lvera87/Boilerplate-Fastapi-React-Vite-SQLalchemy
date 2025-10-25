"""FastAPI application entrypoint."""
from __future__ import annotations

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.api.routes import api_router
from app.core.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import setup_logging

logger = logging.getLogger("app")

limiter = Limiter(key_func=get_remote_address)


def create_app() -> FastAPI:
    settings = get_settings()
    setup_logging()

    application = FastAPI(title=settings.app_name, version=settings.project_version, docs_url="/docs", redoc_url="/redoc")

    # Register custom exception handlers
    register_exception_handlers(application)

    # Add rate limiter state
    application.state.limiter = limiter
    application.add_exception_handler(429, lambda request, exc: {"detail": "Rate limit exceeded"})

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.backend_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix=settings.api_v1_prefix)

    @application.get("/", tags=["root"], summary="Root welcome message")
    async def read_root() -> dict[str, str]:
        return {"message": f"Welcome to {settings.app_name}!"}

    logger.info("Application started in %s mode", settings.environment)
    return application


app = create_app()
