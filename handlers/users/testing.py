from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from states import Test
from aiogram.dispatcher.storage import FSMContext


# Реагирование на команду test. Если не задано состояние, то попадет сюда
@dp.message_handler(Command("test"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование.\n"
                         "'Вопрос №1 \n\n")

    await Test.Question1.set()
    # Перемещение назад
    # await Test.previous()
    # Установка первого состояния
    # await Test.first()


@dp.message_handler(state=Test.Question1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # Первый вариант
    # await state.update_data(answer1=answer)
    # Второй вариант
    # await state.update_data(
    #     {
    #         "answer1": answer
    # }
    # )
    # Третий вариант. Удобен когда нужно изменить данные. Не нужно await
    async with state.proxy() as data:
        data["answer1"] = answer

    await message.answer("Вопрос № 2\n"
                         "Текст вопроса...")

    # Передать следующее состояние
    # Первый способ
    await Test.next()
    # Второй способ
    await Test.Question2.set()


@dp.message_handler(state=Test.Question2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спасибо за ваш ответы")
    await message.answer(f"Ответ 1: {answer1}")
    await message.answer(f"Ответ 2: {answer2}")

    # Сброс состояний
    # await state.finish()
    # Сбросить состояние не теряя данные
    # await state.reset_state(with_data=False)

