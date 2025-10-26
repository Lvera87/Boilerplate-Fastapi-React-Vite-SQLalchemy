"""Authentication service layer."""
from __future__ import annotations

from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User as UserModel
from app.core.security import verify_password, create_access_token


async def authenticate_user(db: AsyncSession, username: str, password: str) -> Optional[UserModel]:
    result = await db.execute(select(UserModel).where(UserModel.username == username))
    user = result.scalar_one_or_none()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


async def create_token_for_user(user: UserModel) -> str:
    payload = {"sub": str(user.id), "username": user.username}
    token = create_access_token(payload)
    return token
