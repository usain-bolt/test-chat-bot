import logging
from aiogram import Bot, Dispatcher, types, executor
from keyboards import start_ikb, ikb_yes_no, ikb_yes_variants, ikb_no_variants
from aiogram.types import InputFile
from aiogram.dispatcher.filters import Text
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TOKEN_API"))
dp = Dispatcher(bot=bot)


async def on_startup(_):
    print("Бот был успешно запущен")


START_TEXT = """
Здравствуйте!\n
Я Ваш виртуальный помощник!\n
И я очень хочу, чтобы мы подружились. Буду рад помочь Вам записаться на платный прием к врачам Республиканской клинической больницы Министерства здравоохранения Республики Татарстан.\n\n
У меня много полезной информации и я очень спешу поделиться ей с Вами!
"""

ABOUT_US = """Сихат РКБ  — подразделение платных услуги Республиканской Клинической Больницы — ведущее 
многопрофильное медицинское учреждение Республики Татарстан """


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=InputFile("images/sihat.png"))
    await bot.send_message(chat_id=message.from_user.id,
                           text=START_TEXT,
                           reply_markup=start_ikb)


@dp.callback_query_handler(Text(equals="start_button"))
async def click_start_button(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Вы уже были на платном приеме в РКБ (Сихат РКБ)?",
                           reply_markup=ikb_yes_no)


@dp.callback_query_handler(Text(equals="yes_btn"))
async def click_yes(callback: types.CallbackQuery):
    await bot.send_message(text="Выберите нужную закладку",
                           chat_id=callback.message.chat.id,
                           reply_markup=ikb_yes_variants)


@dp.callback_query_handler(Text(equals="no_bnt"))
async def click_yes(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.message.chat.id,
                           reply_markup=ikb_no_variants,
                           text="Вы хотите записаться на консультацию или пройти обследование?")


@dp.callback_query_handler(Text(equals="appointment"))
async def appointment(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Написать нам в WhatsApp \n"
                                "https://clck.ru/34GqM2",
                           disable_web_page_preview=True)
    await bot.send_contact(chat_id=callback.message.chat.id,
                           phone_number="+7(843)231-20-90",
                           first_name="Регистратура Сихат РКБ")
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="http://rkb-sihat.ru/",
                           disable_web_page_preview=True)


@dp.callback_query_handler(Text(equals="diagnostics"))
async def click_on_diagnostics(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.message.chat.id,
                           reply_markup=ikb_no_variants,
                           text="Узнайте подробнее")


@dp.callback_query_handler(Text(equals="phone"))
async def send_phone(callback: types.CallbackQuery):
    await bot.send_contact(chat_id=callback.message.chat.id,
                           phone_number="+7(843)231-20-90",
                           first_name="Регистратура Сихат РКБ")


@dp.callback_query_handler(Text(equals="about_us"))
async def about_us(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.message.chat.id,
                           text=ABOUT_US)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
