from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ikb_yes_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Да", callback_data="yes_btn"), InlineKeyboardButton("Нет", callback_data="no_bnt")]
])


start_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Начнем😎', callback_data='start_button')],
    [InlineKeyboardButton('Хочу посмотреть сайт', url='http://rkb-sihat.ru/')],
    [InlineKeyboardButton('Написать нам WhatsApp', url='https://clck.ru/34GqM2')]
])


ikb_yes_variants = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Записаться к специалисту', callback_data='appointment')],
    [InlineKeyboardButton('Записаться на диагностику', callback_data='diagnostics')],
])


ikb_no_variants = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('О нас', callback_data='about_us')],
    [InlineKeyboardButton('Специалисты', url='http://rkb-sihat.ru/platnieuslugi/')],
    [InlineKeyboardButton('Услуги', url='http://rkb-sihat.ru/uslugi/')],
    [InlineKeyboardButton('Позвонить в call-центр', callback_data='phone')],
])


ikb_app = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Да, оставить данные", callback_data="yes_app"),
     InlineKeyboardButton("Нет", callback_data="no_app")]
])