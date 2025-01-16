from aiogram import Router, types
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='Онлайн меню', url='https://cyclone.kg/menu')],
        [types.InlineKeyboardButton(text='Подробнее о нас', url='https://cyclone.kg/')],
        [types.InlineKeyboardButton(text='Оставить отзыв', callback_data='review')]

    ])

    await message.answer(f'Привет {name}\n'
                         f'Мои комманды:\n '
                         f'/start - начать работу с ботом\n'
                         f'/random - случайное блюдо\n'
                         f'/myinfo - информация о пользователе', reply_markup=keyboard)
