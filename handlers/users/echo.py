from loader import dp, bot
from aiogram import types


@dp.message_handler(content_types="text", state=None)
async def bot_echo(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id,
                           text=text)

    # Другие виды записи. Чат id самостоятельно передается
    # await message.answer(text)
    # Отобразит на что отвечаем
    # await message.reply(text)