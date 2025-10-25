"""Integration tests for the health endpoint."""
import pytest


@pytest.mark.anyio
async def test_health_endpoint(async_client) -> None:
    response = await async_client.get("/api/v1/health/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "timestamp" in payload
