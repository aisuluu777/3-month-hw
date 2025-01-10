from aiogram import Router, types
from aiogram.filters import Command
from random import choice

random_router = Router()


@random_router.message(Command('random'))
async def random_food_handler(message: types.Message):
    foods = {
        'pasta': {
            'file': 'images/pasta.jpg',
            'caption': '''репчатый лук – 1 шт.
чеснок – 2 зубчика
оливковое масло – 2 ст. л.
мясной фарш – 600 г
сладкий перец – 2 шт.
консервированные помидоры в собственном соку – 500 г
спагетти – 250 г
тертый твердый сыр – 100 г
орегано, петрушка, базилик – по вкусу
соль, молотый черный перец'''
        },
        'pizza': {
            'file': 'images/pizza.jpg',
            'caption': '''тесто для пиццы 270 - 300 г
соус томатный 100 - 130 г
сыр Моцарелла для пиццы 150 - 180 г
помидоры 1 шт.
базилик зелёный 8-10 листиков
масло оливковое'''
        },
        'ceasar_salad': {
            'file': 'images/Caesar_salad.jpg',
            'caption': '''салат – 160 г
курица (филе) – 200 г
помидоры черри – 100 г
сыр пармезан тертый – 20 г
гренки – 2 горсти
масло оливковое – 4 ст.л.
соль, свежемолотый черный перец по вкусу
Для соуса:
майонез – 150 г
йогурт натуральный – 150 г
каперсы – 20 г
горчица дижонская – 20 г
анчоус (филе) – 100 г'''
        },
        'cheesecake': {
            'file': 'images/Cheesecake.jpg',
            'caption': '''Печенье песочное — 300 г
Масло сливочное — 100 г
Сыр сливочный — 600 г
Сахар — 150 г
Яйца — 3 шт.
Сливки 30-35% — 200 мл'''
        }
    }

    key, menu = choice(list(foods.items()))
    await message.answer_photo(
        photo=types.FSInputFile(menu['file']),
        caption=menu['caption'],
    )
