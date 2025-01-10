from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'Привет {name}\n'
                         f'Мои комманды:\n '
                         f'/start - начать работу с ботом\n'
                         f'/random - случайное блюдо\n'
                         f'/myinfo - информация о пользователе'.format(message.from_user))
