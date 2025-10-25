"""Integration tests for the user endpoints."""
import pytest
from httpx import AsyncClient

from app.db.base import Base
from app.db.session import engine

from app.schemas.user import UserCreate, UserRead

from app.main import app

@pytest.fixture(scope="function", autouse=True)
async def prepare_db():
    """Reset database schema before tests."""
    async with engine.begin() as conn:
        # Drop and recreate all tables
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield

@pytest.mark.anyio
async def test_create_and_get_user(async_client: AsyncClient) -> None:
    user_in = {"username": "alice", "email": "alice@example.com", "full_name": "Alice A.", "password": "secret"}
    # Create user
    response = await async_client.post("/api/v1/users/", json=user_in)
    assert response.status_code == 201
    created: UserRead = UserRead.model_validate(response.json())
    assert created.username == user_in["username"]
    assert created.email == user_in["email"]
    assert created.full_name == user_in["full_name"]
    assert hasattr(created, "id")

    # Get user by ID
    response = await async_client.get(f"/api/v1/users/{created.id}")
    assert response.status_code == 200
    fetched: UserRead = UserRead.model_validate(response.json())
    assert fetched.id == created.id
    assert fetched.username == created.username

@pytest.mark.anyio
async def test_list_users(async_client: AsyncClient) -> None:
    # Crear usuario para listar
    user_in = {"username": "bob", "email": "bob@example.com", "full_name": "Bob B.", "password": "secret2"}
    create_resp = await async_client.post("/api/v1/users/", json=user_in)
    assert create_resp.status_code == 201
    # Listar usuarios
    response = await async_client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(u["username"] == user_in["username"] for u in data)
