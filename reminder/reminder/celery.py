"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""

from __future__ import absolute_import

import asyncio
import os
from celery import Celery
from celery.schedules import crontab
import django
from django.conf import settings

# этот код скопирован с manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reminder.settings")
django.setup()

# здесь вы меняете имя
app = Celery("reminder", broker="redis://localhost:6379/0", broker_connection_retry_on_startup=True)

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = settings.CELERY_BROKER_URL
# celery_event_loop = asyncio.new_event_loop()
# загрузка tasks.py в приложение django
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send_reminder": {"task": "reminder_bot_admin.tasks.send_reminder", "schedule": crontab(minute="*/1")},
}
