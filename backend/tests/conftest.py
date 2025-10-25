"""Pytest fixtures for backend tests."""
from __future__ import annotations

from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient

from app.main import app


@pytest_asyncio.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """Return an HTTPX async client bound to the FastAPI app."""
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client
