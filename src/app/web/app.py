from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.app.aiobot.bot import bot, dp

from src.config import config


@asynccontextmanager
async def lifespan(app: FastAPI) -> ...:
    await bot.set_webhook(
        url=config.webhook.url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    yield
    await bot.delete_webhook()
