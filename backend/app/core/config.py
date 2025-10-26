"""Application settings and configuration helpers."""
from functools import lru_cache
from typing import List

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "FastAPI Boilerplate"
    project_version: str = "0.1.0"
    environment: str = "development"
    # Optional log level used by app.core.logging.setup_logging
    log_level: str | None = None

    api_v1_prefix: str = "/api/v1"
    # Origins allowed to interact with the API (React dev server by default)
    backend_cors_origins: List[str] = ["http://localhost:5173"]

    database_url: str = "sqlite+aiosqlite:///./sql_app.db"
    # JWT / Auth settings
    secret_key: str = "CHANGE_ME_TO_A_RANDOM_SECRET"
    access_token_expire_minutes: int = 60 * 24 * 7  # one week by default
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @field_validator("backend_cors_origins", mode="before")
    @classmethod
    def split_origins(cls, value: List[str] | str) -> List[str]:
        """Ensure CORS origins can be provided as a comma separated string."""
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin]
        return value


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()
