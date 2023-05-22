import logging
from aiogram import bot, types

from aiogram.dispatcher.filters import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # Сохранить имя пользователя в базу
    user_name = message.from_user.full_name

    chat_id = message.chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id,
                           text=text)


# Специальный фильтр для отлова команды /start
# CommandStart()