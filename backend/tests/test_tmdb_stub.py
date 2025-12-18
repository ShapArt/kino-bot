import pytest
from httpx import AsyncClient

from app.main import create_app
from app.config import Settings


class DummySettings(Settings):
    tmdb_api_key: str = "demo"


@pytest.mark.asyncio
async def test_health():
    app = create_app(DummySettings(database_url="", redis_url="", allowed_origins=[], tmdb_api_key="demo"))  # type: ignore[arg-type]
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"
