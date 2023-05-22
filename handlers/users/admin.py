from aiogram import types
from filters import IsPrivate
from loader import dp
from data import config

# список всех фильтров, логика AND если или то делаем сколько раз скоролько или dp.message_handler(фильтр)
@dp.message_handler(IsPrivate(), user_id=config.ADMINS, text="admin")
async def admin_chat_select(message: types.Message):
    await message.answer("Это секретное сообщение, вызванное одним из администроаторов "
                         "в личной переписке")