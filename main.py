import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
from random import choice


token = dotenv_values('.env')['TOKEN']
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'Привет {name}\n'
                         f'Мои комманды:\n '
                         f'/start - начать работу с ботом\n'
                         f'/random - случайное имя\n'
                         f'/myinfo - информация о пользователе'.format(message.from_user))


@dp.message(Command('random'))
async def random_handler(message: types.Message):
    name_list =choice (['Jim', 'Jessie', 'Aisuluu', 'Jasmina', 'Suga','Ronald'])
    await message.answer(f'Случайное имя: {name_list}')


@dp.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    if username is None:
        pass
    await message.answer(f'Ваше имя: {name}\n'
                         f'Ваш username: {username}\n'
                         f'Ваш id: {id}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

