"""Security helpers: password hashing and JWT token creation/verification."""
from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Dict, Optional

from app.core.config import get_settings

# These imports are optional at import-time; if missing, functions will raise
# a clear error explaining what to install.
try:
    from passlib.context import CryptContext
    from jose import JWTError, jwt
except Exception as exc:  # pragma: no cover - dependency guidance
    CryptContext = None  # type: ignore
    JWTError = Exception  # type: ignore
    jwt = None  # type: ignore


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") if CryptContext else None


def verify_password(plain_password: str, hashed_password: str) -> bool:
    if pwd_context is None:
        raise RuntimeError("passlib is required for password hashing; install passlib[bcrypt]")
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    if pwd_context is None:
        raise RuntimeError("passlib is required for password hashing; install passlib[bcrypt]")
    return pwd_context.hash(password)


def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    settings = get_settings()
    if jwt is None:
        raise RuntimeError("python-jose is required for JWT tokens; install python-jose[cryptography]")

    to_encode = data.copy()
    now = datetime.utcnow()
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire, "iat": now})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm="HS256")
    return encoded_jwt


def decode_access_token(token: str) -> Dict[str, Any]:
    settings = get_settings()
    if jwt is None:
        raise RuntimeError("python-jose is required for JWT tokens; install python-jose[cryptography]")
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        return payload
    except JWTError as exc:
        raise
