
from aiogram import Bot, Dispatcher

from bot.config import Config, load_config

configs: Config = load_config()
bot: Bot = Bot(token=configs.bot.token)
dp: Dispatcher = Dispatcher()
