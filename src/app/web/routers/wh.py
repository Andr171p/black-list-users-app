from fastapi import APIRouter, Request

from src.app.aiobot.bot import bot, dp


wh_router = APIRouter(
    prefix="/api/wh"
)


@wh_router.post(path="/webhook")
async def get_webhook(request: Request) -> None:
    update = await request.json()
    await dp.feed_update(
        bot=bot,
        update=update
    )
