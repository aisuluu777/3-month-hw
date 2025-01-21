from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, CallbackQuery


from bot_config import database

review_router = Router()
kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='1', callback_data='rate:1'),
        types.InlineKeyboardButton(text='2', callback_data='rate:2'),
        types.InlineKeyboardButton(text='3', callback_data='rate:3'),
        types.InlineKeyboardButton(text='4', callback_data='rate:4'),
        types.InlineKeyboardButton(text='5', callback_data='rate:5')]

    ])

class RestourantReview(StatesGroup):
    name = State()
    number= State()
    rate = State()
    extra_comments = State()

@review_router.message(Command('stop'))
@review_router.message(F.text == 'стоп')
async def stop_review(message: types.Message, state: FSMContext):
    await message.answer('Диалог остановлен')
    await state.clear()

user = []
@review_router.callback_query(F.data == 'review')
async def review_handler(callback: types.CallbackQuery, state: FSMContext):
         user_id = callback.from_user.id
         if user_id in user:
             await callback.message.answer('Нельзя оставлять отзыв более одного раза!')
             await state.clear()
         else:
             user.append(user_id)
             await callback.message.answer("Оставьте жалобу ответив на несколько вопросов. Можете остановить диалог с ботом введя команду '/stop' или 'стоп'")
             await callback.message.answer('Как вас зовут?')
             await state.set_state(RestourantReview.name)


@review_router.message(RestourantReview.name)
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer('Ваш номер?')
    await state.set_state(RestourantReview.number)


@review_router.message(RestourantReview.number)
async def number_handler(message: types.Message,state: FSMContext):
    number = message.text
    await state.update_data(number=number)
    await message.answer('Как бы вы оценили наш ресторан от 0 до 5?', reply_markup=kb)
    await state.set_state(RestourantReview.rate)


@review_router.callback_query(RestourantReview.rate)
async def rating_handler(callback: CallbackQuery, state: FSMContext):
    rate = callback.data[5:]
    await state.update_data(rate=int(rate))
    await callback.message.answer('Дополнительные комментарии/жалоба?')
    await state.set_state(RestourantReview.extra_comments)


@review_router.message(RestourantReview.extra_comments)
async def extra_handler(message: types.Message, state: FSMContext):
    extra_comments = message.text
    await state.update_data(extra_comments=extra_comments)
    await message.answer(f'Спасибо за оставленный отзыв')
    data = await state.get_data()
    database.save_review(data)
    await state.clear()