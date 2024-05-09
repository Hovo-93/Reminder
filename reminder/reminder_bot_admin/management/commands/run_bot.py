import asyncio
import logging
import signal
import sys

from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from django.core.management.base import BaseCommand

from bot import config
from bot.bot_view import router
from bot.config import dp, bot


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)


class Command(BaseCommand):
    help = "RUN COMMAND: python manage.py run_bot"

    def handle(self, *args, **options):
        asyncio.run(main())
