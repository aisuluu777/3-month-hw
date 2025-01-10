from aiogram import Dispatcher, Bot
from dotenv import dotenv_values


token = dotenv_values('.env')['TOKEN']
bot = Bot(token=token)
dp = Dispatcher()
