import logging
from aiogram import Bot, Dispatcher, types, executor
from keyboards import start_ikb, ikb_yes_no, ikb_yes_variants, ikb_no_variants
from aiogram.types import InputFile
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv, find_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import os
from validate_email import validate_email
import phonenumbers
from send_email import send_mail


load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO)


storage = MemoryStorage()
bot = Bot(token=os.getenv("TOKEN_API"))
dp = Dispatcher(bot=bot,
                storage=storage)


class FormAppointment(StatesGroup):
    """"""
    user_name = State()
    user_email = State()
    user_phone = State()


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
                         photo=InputFile("data/images/sihat.png"))
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
                           text="Что Вы хотели бы узнать?")


@dp.callback_query_handler(Text(equals="app_online"))
async def send_name_question(callback: types.CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=callback.from_user.id,
                           text="Напишите, пожалуйста, ФИО полностью")

@dp.message_handler()
async def enter_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Укажите пожалуйста Вашу электронную почту?")
    await FormAppointment.user_email.set()


@dp.message_handler(state=FormAppointment.user_email)
async def enter_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    # try:
    #     e
    await message.answer("Укажите Ваш контактный телефон?")
    await FormAppointment.next()


@dp.message_handler(state=FormAppointment.user_phone)
async def enter_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

    async with state.proxy() as data:
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        send_mail(name, email, phone)

    await message.answer("Благодарим за предоставленную информацию.\n"
                         "Мы с Вами свяжемся")
    await state.finish()


@dp.callback_query_handler(Text(equals="app_online"))
async def send_phone(callback: types.CallbackQuery):
    await bot.send_contact(chat_id=callback.message.chat.id,
                           phone_number="+7(843)231-20-90",
                           first_name="Регистратура Сихат РКБ")


@dp.callback_query_handler(Text(equals="phone"))
async def send_phone(callback: types.CallbackQuery):
    await bot.send_contact(chat_id=callback.message.chat.id,
                           phone_number="+7(843)231-20-90",
                           first_name="Регистратура Сихат РКБ")


@dp.callback_query_handler(Text(equals="about_us"))
async def about_us(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.message.chat.id,
                           text=ABOUT_US)


@dp.callback_query_handler(Text(equals="telegram"))
async def get_telegram(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="@sihat_rch")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
