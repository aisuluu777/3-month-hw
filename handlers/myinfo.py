from aiogram import Router, types
from aiogram.filters import Command

myinfo_router = Router()


@myinfo_router.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username if message.from_user.username else "Отсутвует username"
    if username is None:
        print('У вас нет username!')
    await message.answer(f'Ваше имя: {name}\n'
                         f'Ваш username: {username}\n'
                         f'Ваш id: {id}')
