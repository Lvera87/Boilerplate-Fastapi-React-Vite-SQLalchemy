"""Healthcheck endpoint."""
from datetime import datetime, timezone

from fastapi import APIRouter

from app.db.session import get_async_engine
from app.schemas.health import DatabaseStatus, HealthResponse

router = APIRouter()


@router.get("/", response_model=HealthResponse, summary="Service healthcheck")
async def get_health() -> HealthResponse:
    """Return service status and metadata including database connection."""
    db_status = None

    try:
        engine = get_async_engine()
        async with engine.begin() as conn:
            await conn.execute(conn.exec("SELECT 1"))
        db_status = DatabaseStatus(connected=True)
    except Exception:
        db_status = DatabaseStatus(connected=False)

    return HealthResponse(
        status="ok" if db_status.connected else "degraded",
        timestamp=datetime.now(timezone.utc),
        database=db_status,
    )
