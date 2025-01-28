from aiogram import F, types, Router
from bot_config import database
from aiogram_widgets.pagination import TextPaginator

dish_router = Router()


@dish_router.callback_query(F.data == 'dish')
async def dish_handler(callback: types.CallbackQuery):
    await callback.message.answer('Our catalog of food')
    food_list = database.get_all_dishes()

    text_data = [f'Название: {dish.get("name")}\n'
                 f'Цена: {dish.get("price")}\n'
                 f'Описание: {dish.get("caption")}\n'
                 f'Категория: {dish.get("category")}\n'
                 f'Порция: {dish.get("portions")}' for dish in food_list]


    paginator = TextPaginator(data=text_data, router=dish_router, per_page=1)
    current_text_chunk, reply_markup = paginator.current_message_data


    await callback.message.answer(
           text=current_text_chunk,
                 reply_markup=reply_markup
                 )