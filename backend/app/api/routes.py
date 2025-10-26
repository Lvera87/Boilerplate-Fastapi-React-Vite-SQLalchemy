"""Collect and expose API routers."""
from fastapi import APIRouter

from app.api.endpoints import health, users, auth

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"]) 
