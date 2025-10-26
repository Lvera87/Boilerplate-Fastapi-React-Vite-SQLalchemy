"""User CRUD endpoints."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_async_session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate, UserRead
from app.core.security import get_password_hash

router = APIRouter(tags=["users"])


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_async_session)) -> UserRead:
    """Create a new user in the database."""
    user = UserModel(
        username=user_in.username,
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=get_password_hash(user_in.password),
    )
    db.add(user)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Username or email already exists")
    await db.refresh(user)
    return user


@router.get("/", response_model=List[UserRead])
async def list_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_session)) -> List[UserRead]:
    """Retrieve list of users."""
    result = await db.execute(select(UserModel).offset(skip).limit(limit))
    users = result.scalars().all()
    return users


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, db: AsyncSession = Depends(get_async_session)) -> UserRead:
    """Get a single user by ID."""
    result = await db.execute(select(UserModel).where(UserModel.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
