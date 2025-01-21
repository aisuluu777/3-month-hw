from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

users = []
@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    if user_id not in users:
        users.append(user_id)
        counter = len(users)

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text='Онлайн меню', url='https://cyclone.kg/menu')],
            [types.InlineKeyboardButton(text='Подробнее о нас', url='https://cyclone.kg/')],
            [types.InlineKeyboardButton(text='Оставить отзыв', callback_data='review')]

        ])

    await message.answer(f'Привет {name}\n'
                         f'Наш бот обслуживает уже {counter} пользователя\n'
                         f'Мои комманды:\n '
                         f'/start - начать работу с ботом\n'
                         f'/random - случайное блюдо\n'
                         f'/myinfo - информация о пользователе', reply_markup=keyboard)
