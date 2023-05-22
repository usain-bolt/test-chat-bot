from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    import filters
    import middlewares
    filters.setup(dispatcher)
    middlewares.setup(dispatcher)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
