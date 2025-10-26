"""Pytest fixtures for backend tests."""
from __future__ import annotations

from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient
try:
    # Newer httpx versions require an explicit ASGITransport for app-based testing
    from httpx import ASGITransport
except Exception:  # pragma: no cover - compatibility for different httpx versions
    ASGITransport = None

from app.main import app


@pytest_asyncio.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """Return an HTTPX async client bound to the FastAPI app."""
    # Use ASGITransport when available; otherwise fall back to app=... if httpx supports it
    if ASGITransport is not None:
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://testserver") as client:
            yield client
    else:
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            yield client
