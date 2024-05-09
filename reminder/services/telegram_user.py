import logging

from asgiref.sync import sync_to_async
from django.core.exceptions import MultipleObjectsReturned
from reminder_bot_admin.models import TelegramUser


class TelegramUserDao:

    @classmethod
    @sync_to_async
    def create_telegram_user(cls, telegram_id, name, full_name):
        try:
            tg_user = TelegramUser.objects.filter()
            if tg_user.exists():
                logging.info("Candidate already exists!")
                return tg_user.first()
            else:
                new_candidate = TelegramUser.objects.create(telegram_id=telegram_id, name=name, full_name=full_name)
                logging.info("Candidate created!")
                return new_candidate
        except MultipleObjectsReturned:
            logging.error("Multiple candidates found for the given criteria!")
            return None
        except Exception as e:
            logging.error(f"Error creating candidate: {e}")
            return None