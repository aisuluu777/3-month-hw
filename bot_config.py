from aiogram import Dispatcher, Bot
from dotenv import dotenv_values
from database import Database


token = dotenv_values('.env')['TOKEN']
bot = Bot(token=token)
dp = Dispatcher()
database = Database('db.sqlite3')

