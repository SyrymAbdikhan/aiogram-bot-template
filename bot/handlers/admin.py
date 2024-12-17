
from aiogram import Router
from aiogram.types import Message

from bot import configs
from bot.filters import IsBotAdminFilter

admin_router: Router = Router()
admin_router.message.filter(IsBotAdminFilter(configs.bot.admin_ids))


@admin_router.message()
async def process_any_admin_message(message: Message):
    await message.reply(f'admin! {message.text}')
