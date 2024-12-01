from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class WebAppConfig(BaseSettings):
    templates: Path = BASE_DIR / "src" / "app" / "web" / "static" / "templates"


class SQLiteConfig(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/src/database/data/black-list.db"


class Config(BaseSettings):
    sqlite: SQLiteConfig = SQLiteConfig()
    web_app: WebAppConfig = WebAppConfig()


config = Config()
