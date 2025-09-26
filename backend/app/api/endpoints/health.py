"""Healthcheck endpoint."""
from datetime import datetime, timezone

from fastapi import APIRouter

from app.schemas.health import HealthResponse

router = APIRouter()


@router.get("/", response_model=HealthResponse, summary="Service healthcheck")
async def get_health() -> HealthResponse:
    """Return service status and metadata."""
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(timezone.utc),
    )
