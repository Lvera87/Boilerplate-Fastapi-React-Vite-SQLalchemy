"""Rate limiting configuration for API."""
from __future__ import annotations

from slowapi import Limiter
from slowapi.util import get_remote_address


def get_limiter() -> Limiter:
    """Create and return a rate limiter instance."""
    return Limiter(key_func=get_remote_address)
