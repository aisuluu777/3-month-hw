import asyncio

from bot_config import bot, dp
from handlers.start import start_router
from handlers.random_photo import random_router
from handlers.myinfo import myinfo_router
from handlers.review_dialog import review_router
import logging


async def main():
    dp.include_router(start_router)
    dp.include_router(random_router)
    dp.include_router(myinfo_router)
    dp.include_router(review_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


