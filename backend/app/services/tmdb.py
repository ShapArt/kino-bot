from typing import Any, Dict, List

import httpx

TMDB_BASE_URL = "https://api.themoviedb.org/3"


class TmdbClient:
    def __init__(self, api_key: str, language: str = "ru-RU") -> None:
        self.api_key = api_key
        self.language = language

    async def search_movies(self, query: str) -> List[Dict[str, Any]]:
        params = {"query": query, "api_key": self.api_key, "language": self.language}
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(f"{TMDB_BASE_URL}/search/movie", params=params)
            resp.raise_for_status()
            data = resp.json()
            return data.get("results", [])

    async def get_movie(self, movie_id: int) -> Dict[str, Any]:
        params = {"api_key": self.api_key, "language": self.language}
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(f"{TMDB_BASE_URL}/movie/{movie_id}", params=params)
            resp.raise_for_status()
            return resp.json()
