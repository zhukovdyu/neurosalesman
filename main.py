import asyncio
from create_bot import bot, dp
from start_cmd import start_cmd_router
from chat_handler import chat_handler_router

async def run_telegram_bot():
    """Run the Telegram bot polling."""
    await dp.start_polling(bot, skip_updates=True)

async def run():
    # Run both the FastAPI server and Telegram bot concurrently
    await asyncio.gather(
        run_telegram_bot(),  # Start the Telegram bot
    )

async def amain():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':

    dp.include_router(start_cmd_router)
    dp.include_router(chat_handler_router)
    print("commands registered")

    try:
        asyncio.run(run())
        print("Application started.")
    except KeyboardInterrupt:
        print("Application stopped.")
