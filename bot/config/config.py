
import json
from dataclasses import dataclass

from dotenv import load_dotenv

from .base import getenv


@dataclass
class Bot:
    token: str
    admin_ids: list[int]
    allowed_updates: list[str]


@dataclass
class Webhook:
    host: str
    path: str
    port: int
    secret: str
    base_url: str
    
    @property
    def url(self):
        return self.base_url + self.path


@dataclass
class Config:
    bot: Bot
    webhook: Webhook


def load_config() -> Config:
    load_dotenv()
    return Config(
        bot=Bot(
            token=getenv('BOT_TOKEN'),
            admin_ids=getenv('BOT_ADMIN_IDS', json.loads),
            allowed_updates=getenv('ALLOWED_UPDATES', json.loads),
        ),
        webhook=Webhook(
            host=getenv('WEB_SERVER_HOST'),
            path=getenv('WEBHOOK_PATH'),
            port=getenv('WEB_SERVER_PORT', int),
            secret=getenv('WEBHOOK_SECRET'),
            base_url=getenv('BASE_WEBHOOK_URL')
        )
    )
