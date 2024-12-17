
from aiogram import Dispatcher

from .admin import admin_router
from .echo import echo_router


async def register_routers(dp: Dispatcher) -> None:
    dp.include_routers(admin_router, echo_router)
