
from aiogram import Router
from aiogram.types import Message

echo_router: Router = Router()


@echo_router.message()
async def process_any_message(message: Message):
    await message.reply(message.text)
