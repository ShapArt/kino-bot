from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "kino-bot-backend"
    tmdb_api_key: str = Field(..., alias="TMDB_API_KEY")
    database_url: str = Field(..., alias="DATABASE_URL")
    redis_url: str = Field(..., alias="REDIS_URL")
    allowed_origins: list[str] = Field(default_factory=lambda: ["*"], alias="ALLOWED_ORIGINS")


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[arg-type]


SettingsDep = Annotated[Settings, Depends(get_settings)]
