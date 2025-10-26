"""Database session management."""
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings
from typing import AsyncGenerator

settings = get_settings()

# Lazily create the engine to avoid requiring DB driver packages during
# import-time (useful for lightweight test environments).
_engine = None

def get_async_engine():
    """Return a lazily-initialized AsyncEngine instance."""
    global _engine
    if _engine is None:
        _engine = create_async_engine(
            settings.database_url,
            echo=True,
            future=True,
        )
    return _engine


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Yield a database session in async context."""
    engine = get_async_engine()
    AsyncSessionLocal = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with AsyncSessionLocal() as session:
        yield session
