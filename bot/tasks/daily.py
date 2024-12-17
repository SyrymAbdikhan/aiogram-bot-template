
import asyncio


async def action() -> None:
    while True:
        await asyncio.sleep(24*60*60)
        # do something every 24 hours
