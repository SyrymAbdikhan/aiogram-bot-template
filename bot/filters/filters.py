
from aiogram.filters import Filter
from aiogram.types import Message


class IsBotAdminFilter(Filter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        if message.from_user.id in self.admin_ids:
            return True
        return False
