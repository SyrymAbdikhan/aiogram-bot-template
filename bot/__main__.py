
import asyncio
import logging

from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram import Dispatcher
from aiogram.types import BotCommand

from bot import bot, dp, configs
from bot.handlers import register_routers
from bot.tasks import register_tasks

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] #%(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot")

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    if configs.webhook.base_url:
        run_webhook()
    else:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(run_poller())


async def run_poller() -> None:
    await dp.start_polling(
        bot,
        skip_updates=True,
        allowed_updates=configs.bot.allowed_updates
    )


def run_webhook() -> None:
    webhook = configs.webhook
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=webhook.secret
    )
    webhook_requests_handler.register(app, path=webhook.path)

    setup_application(app, dp, bot=bot)
    web.run_app(app, host=webhook.host, port=webhook.port)


async def on_startup(dispatcher: Dispatcher) -> None:
    await initialize_bot(dispatcher)

    webhook = configs.webhook
    if webhook.base_url:
        await bot.set_webhook(
            webhook.url,
            secret_token=webhook.secret,
            allowed_updates=configs.bot.allowed_updates,
            drop_pending_updates=True
        )
        logger.info('Webhook was set')
    else:
        await bot.delete_webhook(drop_pending_updates=True)
        logger.info('Webhook was deleted')

    logger.info('Bot started!')


async def on_shutdown(dispatcher: Dispatcher) -> None:
    await dispatcher.storage.close()
    logger.info('Bot shutdown!')


async def initialize_bot(dispatcher: Dispatcher) -> None:
    await register_commands()
    await register_routers(dispatcher)
    register_tasks()


async def register_commands() -> None:
    commands = [
        # BotCommand(command='/start', description='...'),
    ]
    await bot.set_my_commands(commands)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
