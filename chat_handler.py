import asyncio
import requests
from datetime import datetime
from aiogram import F, Router
from aiogram import types
import json
import requests
import os
from aiogram.fsm.context import FSMContext
import aiohttp
from gpt_model import llm

chat_handler_router = Router()

@chat_handler_router.message(F.text)
async def request_in_chatgpt_cmd(message: types.Message, state: FSMContext):
    answer = llm.answer_question(message.text)
    # Добавляем вопрос и ответ в историю
    llm.history.append({"role": "user", "content": message.text})
    llm.history.append({"role": "assistant", "content": answer})
    print(f'History: {llm.history}')
    await message.answer(answer)

def register_default_handler_cmd(dp):
    dp.include_router(chat_handler_router)
