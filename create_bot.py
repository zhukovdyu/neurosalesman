from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
import os
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv('TELEGRAM__TELEGRAM_BOT_TOKEN')
print(f"Bot token: {bot_token}")

bot = Bot(
    token=bot_token,
    default=DefaultBotProperties(
        parse_mode=ParseMode.MARKDOWN
        )
)

dp = Dispatcher(storage=MemoryStorage())
