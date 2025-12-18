from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .config import Settings, get_settings
from .services.tmdb import TmdbClient


class Movie(BaseModel):
    id: int
    title: str
    overview: str | None = None
    poster_path: str | None = Field(default=None, description="TMDB poster path")
    release_date: str | None = None
    vote_average: float | None = None


class SearchResponse(BaseModel):
    results: list[Movie]


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(title=settings.app_name)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/tmdb/search", response_model=SearchResponse)
    async def tmdb_search(
        q: str, settings_dep: Annotated[Settings, Depends(get_settings)]  # type: ignore
    ) -> SearchResponse:
        if not q:
            raise HTTPException(status_code=400, detail="Query is required")
        client = TmdbClient(settings_dep.tmdb_api_key)
        data = await client.search_movies(q)
        results = [
            Movie(
                id=item.get("id"),
                title=item.get("title", ""),
                overview=item.get("overview"),
                poster_path=item.get("poster_path"),
                release_date=item.get("release_date"),
                vote_average=item.get("vote_average"),
            )
            for item in data
        ]
        return SearchResponse(results=results)

    @app.get("/tmdb/movie/{movie_id}", response_model=Movie)
    async def tmdb_movie(
        movie_id: int, settings_dep: Annotated[Settings, Depends(get_settings)]  # type: ignore
    ) -> Movie:
        client = TmdbClient(settings_dep.tmdb_api_key)
        data = await client.get_movie(movie_id)
        return Movie(
            id=data.get("id"),
            title=data.get("title", ""),
            overview=data.get("overview"),
            poster_path=data.get("poster_path"),
            release_date=data.get("release_date"),
            vote_average=data.get("vote_average"),
        )

    return app


def get_app() -> FastAPI:
    return create_app(get_settings())


app = get_app()
