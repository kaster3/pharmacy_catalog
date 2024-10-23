from pathlib import Path
from typing import Literal

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    endpoint: str = "/endpoint"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class LoggingConfig(BaseModel):
    log_level: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"
    log_format: str


class DataBase(BaseModel):
    url: PostgresDsn
    echo: bool
    echo_pool: bool
    pool_size: int
    max_overflow: int

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class RunConfig(BaseModel):
    app: str
    host: str
    port: int
    reload: bool
    workers: int


class GunicornConfig(BaseModel):
    host: str
    port: int
    workers: int
    timeout: int


class JWTToken(BaseModel):
    public_key: Path = BASE_DIR / "certs" / "jwt-public-key.pem"
    algorithm: str = "RS256"
    audience: str = "fastapi-users:auth"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
    )
    conf: RunConfig
    gunicorn: GunicornConfig
    db: DataBase
    logging: LoggingConfig
    api: ApiPrefix = ApiPrefix()
    jwt_token: JWTToken = JWTToken()


settings = Settings()
