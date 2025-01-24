from aiogram import types, Router, F
from aiogram.filters import Command

from bot_config import database

check_review_router = Router()
check_review_router.message.filter(
    F.from_user.id ==  5947069782
)

@check_review_router.message(Command('check'))
async def start_review(message: types.Message):
    await message.answer('Отзывы:')
    review_list = database.get_all_reviews()
    for review in review_list:
        await message.answer(f'имя пользователя: {review.get("name")}\n'
                             f'Отзыв: {review.get("extra_comments")}\n')