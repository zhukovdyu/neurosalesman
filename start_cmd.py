from aiogram import F, Router
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
import aiohttp
import os
import json
from gpt_model import llm

start_cmd_router = Router()

@start_cmd_router.message(CommandStart())
async def start_cmd(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    print(f'User {user_id} started the bot')
    chat_message = llm.answer_question(message.text)
    llm.history.append({"role": "user", "content": message.text})
    llm.history.append({"role": "assistant", "content": chat_message})
    print(f'History: {llm.history}')
    await message.answer(chat_message)


def register_start_cmd(dp):
    dp.include_router(start_cmd_router)
