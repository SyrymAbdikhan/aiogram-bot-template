
import asyncio

from .daily import action


def register_tasks() -> None:
    asyncio.ensure_future(action())
