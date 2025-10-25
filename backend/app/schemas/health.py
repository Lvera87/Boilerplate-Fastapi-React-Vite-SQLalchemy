"""Response schemas for health endpoints."""
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


class DatabaseStatus(BaseModel):
    """Database status details."""

    connected: bool
    engine: str = "SQLite (Async)"


class HealthResponse(BaseModel):
    """Healthcheck response payload."""

    status: Literal["ok", "degraded"]
    timestamp: datetime
    database: DatabaseStatus | None = None

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "status": "ok",
                    "timestamp": "2023-01-01T00:00:00Z",
                    "database": {"connected": True, "engine": "SQLite (Async)"},
                }
            ]
        }
    )
