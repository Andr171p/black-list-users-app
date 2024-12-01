import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class WebhookConfig(BaseSettings):
    url: str = os.getenv("TUNA_URL")


class WebAppConfig(BaseSettings):
    templates: Path = BASE_DIR / "src" / "app" / "web" / "static" / "templates"


class BotConfig(BaseSettings):
    token: str = os.getenv("BOT_TOKEN")


class SQLiteConfig(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/src/database/data/black-list.db"


class Config(BaseSettings):
    bot: BotConfig = BotConfig()
    sqlite: SQLiteConfig = SQLiteConfig()
    web_app: WebAppConfig = WebAppConfig()
    webhook: WebhookConfig = WebhookConfig()

    def get_webhook_url(self) -> str:
        return f"{self.webhook.url}/webhook"


config = Config()
