from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from bot_config import database

food_router = Router()
food_router.message.filter(
    F.from_user.id == 5947069782
)

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='первое', callback_data='первое')],
    [InlineKeyboardButton(text='второе', callback_data='второе')],
    [InlineKeyboardButton(text='пицца', callback_data='пицца')],
    [InlineKeyboardButton(text='горячие напитки', callback_data='горячие напитки')],
    [InlineKeyboardButton(text='холодные напитки', callback_data='холодные напитки')],
    [InlineKeyboardButton(text='Десерт', callback_data='Дессерт')]
])

class AddFood(StatesGroup):
    name = State()
    price = State()
    caption = State()
    category = State()
    portion = State()




@food_router.message(Command('stop'))
@food_router.message(F.text == 'стоп')
async def stop(message: types.Message, state: FSMContext):
    await message.answer('Диалог остановлен')
    await state.clear()


@food_router.message(Command('addfood'))
async def start_proces(message: types.Message, state: FSMContext):
    await message.answer('Напишите названия блюда.')
    await state.set_state(AddFood.name)


@food_router.message(AddFood.name)
async def name_proces(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Напишите цену блюда.')
    await state.set_state(AddFood.price)



@food_router.message(AddFood.price)
async def price_proces(message: types.Message, state: FSMContext):
    price = message.text
    if not price.isdigit():
        await message.answer('Вводите только цифры!')
        return
    price = int(price)
    if price <= 0:
        await message.answer('Вводите только положительную сумму!')
        return
    await state.update_data(price=message.text)
    await message.answer('Напишите описание блюда.')
    await state.set_state(AddFood.caption)


@food_router.message(AddFood.caption)
async def caption_proces(message: types.Message, state: FSMContext):
    await state.update_data(caption=message.text)
    await message.answer('Напишите категорию блюда.', reply_markup=keyboard)
    await state.set_state(AddFood.category)


@food_router.callback_query(AddFood.category)
async def category_proces(callback: CallbackQuery, state: FSMContext):
    category = callback.data
    await state.update_data(category=category)
    await callback.message.answer('Напишите порцию блюда.')
    await state.set_state(AddFood.portion)


@food_router.message(AddFood.portion)
async def portion_proces(message: types.Message, state: FSMContext):
    portion = message.text
    if not portion.isdigit():
        await message.answer('Вводите только цифры!')
        return
    portion = int(portion)
    if portion <= 0:
        await message.answer('Вводите только положительное число!')
        return
    await state.update_data(portions=message.text)
    await message.answer('Спасибо блюдо было сохранена')
    data = await state.get_data()
    print(data)
    database.save_dishes(data)
    await state.clear()



