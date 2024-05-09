from datetime import datetime

from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,

)
from aiogram import Router

from open_ai.time_parser import TextParser
from services.reminder import ReminderDao
from services.telegram_user import TelegramUserDao
from . import messages


from dotenv import load_dotenv

load_dotenv()
router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n\n{messages.WELCOME_MESSAGE}", parse_mode=ParseMode.HTML
    )


@router.message()
async def handle_user_message(message: Message):
    tg_user = await TelegramUserDao.create_telegram_user(
        telegram_id=message.chat.id, full_name=message.chat.full_name, name=message.chat.username
    )
    reminder_text = message.text
    open_ai_response = TextParser().analyze_text_and_extract_info(reminder_text)
    date_time = datetime.strptime(open_ai_response, "%Y-%m-%d %H:%M")
    await ReminderDao.create_reminder(user=tg_user, text=reminder_text, reminder_date_time=date_time)

    await message.reply("Я создал напоминание для вас!")
