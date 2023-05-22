import logging

from aiogram.types import Update

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                          CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                          MessageTextIsEmpty, RetryAfter,
                                          CantParseEntities, MessageCantBeDeleted, BadRequest)

    if isinstance(exception, CantDemoteChatCreator):
        logging.debug("Не удается понизить роль создателя чата")
        return True

    if isinstance(exception, MessageNotModified):
        logging.debug("сообщение не изменено")
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.debug("Cообщение не может быть удалено")
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.debug("Не найдено сообщение к удалению")
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.debug("Текстовое сообщение пустое")
        return True

    if isinstance(exception, Unauthorized):
        logging.debug(f"Unauthorized {exception}")
        return True

    if isinstance(exception, InvalidQueryID):
        logging.debug(f"InvalidQueryID {exception} \n Update: {update}")
        return True

    if isinstance(exception, CantParseEntities):
        await Update.get_current().message.answer(f"Попало в эррор хендлер. CantParseEntities: {exception}")
        return True

    if isinstance(exception, RetryAfter):
        logging.debug(f"RetryAfter: {exception}\n Update: {update}")
        return True

    if isinstance(exception, BadRequest):
        logging.debug(f"CantParseEntities: {exception}\n Update: {update}")
        return True

    if isinstance(exception, TelegramAPIError):
        logging.debug(f"TelegramAPIError: {exception}\n Update: {update}")
        return True

    logging.exception(f"Update {update} \n {exception}")


