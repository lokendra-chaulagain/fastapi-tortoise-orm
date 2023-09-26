from typing import Set
from pydantic_settings import BaseSettings


class EnvironmentSettings(BaseSettings):
    API_VERSION: str = "v1"
    APP_NAME: str = "HMS"
    TEST_DATABASE_URL: str = ""
    POSTGRES_DB_URL: str = "postgres://higtyzzf:lWbxTPVjPlhBt5fLQCOJGglQpPwk6pVh@peanut.db.elephantsql.com/higtyzzf"
    DEBUG_MODE: bool = False
    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str = ""
    ALLOWED_ORIGINS: list[str] = []


settings = EnvironmentSettings()
