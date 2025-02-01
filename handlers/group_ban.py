from aiogram import types, F, Router
from banned_words import ban_words



ban_router = Router()
ban_router.message.filter(F.chat.type != 'private')



@ban_router.message(F.text)
async def ban_handler(message: types.Message):
    if message:
        user_id = message.from_user.id
        for word in ban_words:
            if word in message.text.lower():
                await message.chat.ban(user_id)


