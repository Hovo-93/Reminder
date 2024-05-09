import asyncio
import datetime
import logging
from datetime import timezone

from asgiref.sync import async_to_sync, sync_to_async
from aiogram.methods.send_message import SendMessage
from bot.config import bot, dp
from reminder.celery import app

from tqdm import tqdm

from reminder_bot_admin.models import (
    Reminder, TelegramUser, StatusChoices
)
from services.reminder import ReminderDao


async def sender():

    current_time = datetime.datetime.now()

    user, text = await ReminderDao.get_pending_reminder(current_time=current_time)

    await bot.send_message(chat_id=user, text=f"Привет, ты просил напомнить что: {text}")
    await ReminderDao.change_status(user=user)


@app.task
def send_reminder() -> None:
    asyncio.get_event_loop().run_until_complete(sender())
