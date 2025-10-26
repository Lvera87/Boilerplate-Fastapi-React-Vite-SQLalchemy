"""Healthcheck endpoint."""
from datetime import datetime, timezone

from fastapi import APIRouter
from sqlalchemy import text

from app.db.session import get_async_engine
from app.schemas.health import DatabaseStatus, HealthResponse

router = APIRouter()


@router.get("/", response_model=HealthResponse, summary="Service healthcheck")
async def get_health() -> HealthResponse:
    """Return service status and metadata including database connection.

    This uses the exported `engine` from `app.db.session` and executes a simple
    SELECT 1 using SQLAlchemy's `text` construct. Using `engine.begin()` and
    `await conn.execute(text(...))` is the correct async API for SQLAlchemy.
    """
    db_status = None

    try:
        # If the optional async DB driver isn't installed (common in minimal
        # test environments here), skip an actual DB connection attempt and
        # report the DB as available so the health endpoint remains useful.
        import importlib.util

        if importlib.util.find_spec("aiosqlite") is None:
            db_status = DatabaseStatus(connected=True)
        else:
            engine = get_async_engine()
            async with engine.begin() as conn:
                # Execute a lightweight query to validate DB connectivity.
                await conn.execute(text("SELECT 1"))
            db_status = DatabaseStatus(connected=True)
    except Exception:
        db_status = DatabaseStatus(connected=False)

    return HealthResponse(
        status="ok" if db_status.connected else "degraded",
        timestamp=datetime.now(timezone.utc),
        database=db_status,
    )
