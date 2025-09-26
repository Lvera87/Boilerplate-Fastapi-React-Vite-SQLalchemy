"""Response schemas for health endpoints."""
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    """Healthcheck response payload."""

    status: Literal["ok"]
    timestamp: datetime

    model_config = ConfigDict(json_schema_extra={"examples": [{"status": "ok", "timestamp": "2023-01-01T00:00:00Z"}]})
