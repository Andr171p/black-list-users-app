from fastapi import FastAPI, Request

from src.app.aiobot.bot import bot, dp
from src.app.web.app import lifespan


app = FastAPI(
    title="black-list-app",
    lifespan=lifespan
)


@app.post(path="/webhook")
async def get_webhook(request: Request) -> None:
    update = await request.json()
    await dp.feed_update(
        bot=bot,
        update=update
    )