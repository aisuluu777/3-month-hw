from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

review_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    instagram_username = State()
    rate = State()
    extra_comments = State()


@review_router.callback_query(F.data == 'review')
async def review_handler(callback: types.CallbackQuery, state: FSMContext):
    user = await state.get_data()
    if user.get('reviewed'):
        await callback.message.answer('Нельзя оставлять отзыв более одного раза.')
        await state.clear()
    else:
        await callback.message.answer('Как вас зовут?')
        await state.set_state(RestourantReview.name)


@review_router.message(RestourantReview.name)
async def review_handler(message: types.Message, state: FSMContext):
    await message.answer('Ваш инстаграм аккаунт?')
    await state.set_state(RestourantReview.instagram_username)


@review_router.message(RestourantReview.instagram_username)
async def review_handler(message: types.Message, state: FSMContext):
    await message.answer('Как бы вы оценили наш ресторан от 0 до 5?')
    await state.set_state(RestourantReview.rate)


@review_router.message(RestourantReview.rate)
async def review_handler(message: types.Message, state: FSMContext):
    await message.answer('Дополнительные комментарии/жалоба?')
    await state.set_state(RestourantReview.extra_comments)


@review_router.message(RestourantReview.extra_comments)
async def review_handler(message: types.Message, state: FSMContext):
    await message.answer('Спасибо за оставленный отзыв')
    await state.update_data(reviewed=True)
    await state.clear()


