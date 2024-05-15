from enum import Enum

from pydantic_settings import BaseSettings


class Environment(str, Enum):
    PRODUCTION = "prod"
    DEVELOPMENT = "dev"


class Settings(BaseSettings):
    SQLITEDB_PATH: str = "filmswap.db"
    SQL_ECHO: bool = False
    GUILD_ID: int = -1
    ALLOWED_ROLES: list[str] = []
    ENVIRONMENT: str = Environment.DEVELOPMENT
    BACKUP_DIR: str = "backups"
    BOT_NAME: str = "FilmSwap"
    PERIOD_POST_HOOK: bool = True
    FILMSWAP_TOKEN: str
    BACKUPS_DIR: str = "backups"

    class Config:
        case_sensitive = False
        env_file = ".env"


settings = Settings()
