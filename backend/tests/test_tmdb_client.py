import pytest

from app.services.tmdb import TmdbClient


class DummyResponse:
    def __init__(self, json_data: dict, status_code: int = 200) -> None:
        self._json = json_data
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise RuntimeError("error")

    def json(self) -> dict:
        return self._json


class DummyClient:
    def __init__(self, data: dict) -> None:
        self.data = data

    async def get(self, *args, **kwargs):
        return DummyResponse(self.data)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False


@pytest.mark.asyncio
async def test_search_movies(monkeypatch):
    client = TmdbClient(api_key="demo")
    payload = {"results": [{"id": 1, "title": "Test"}]}

    async def fake_async_client(*args, **kwargs):
        return DummyClient(payload)

    monkeypatch.setattr("httpx.AsyncClient", fake_async_client)
    results = await client.search_movies("q")
    assert results[0]["title"] == "Test"


@pytest.mark.asyncio
async def test_get_movie(monkeypatch):
    client = TmdbClient(api_key="demo")
    payload = {"id": 42, "title": "Movie"}

    async def fake_async_client(*args, **kwargs):
        return DummyClient(payload)

    monkeypatch.setattr("httpx.AsyncClient", fake_async_client)
    movie = await client.get_movie(42)
    assert movie["id"] == 42
