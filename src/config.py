from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class WebAppConfig(BaseSettings):
    templates: Path = BASE_DIR / "src" / "app" / "web" / "static" / "templates"


class Config(BaseSettings):
    web_app: WebAppConfig = WebAppConfig()


config = Config()
