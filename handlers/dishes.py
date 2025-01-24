from aiogram import F, types, Router
from bot_config import database


dish_router = Router()

@dish_router.callback_query(F.data == 'dish')
async def dish_handler(callback: types.CallbackQuery):
    await callback.message.answer('Our catalog of food')
    food_list = database.get_all_dishes()
    for dish in food_list:
     await callback.message.answer(f'Название: {dish.get("name")}\n'
                                  f'Цена: {dish.get("price")}\n'
                                  f'Описание: {dish.get("caption")}\n'
                                  f'Категория: {dish.get("category")}\n'
                                  f'Порция: {dish.get("portions")}\n')



