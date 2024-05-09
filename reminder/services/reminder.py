import logging

from asgiref.sync import sync_to_async

from reminder_bot_admin.models import Reminder, StatusChoices


class ReminderDao:
    @classmethod
    @sync_to_async
    def create_reminder(cls, user, text, reminder_date_time):
        try:
            Reminder.objects.create(user=user, text=text, reminder_date_time=reminder_date_time)
            logging.info("Candidate created!")
        except Exception as e:
            logging.error(f"Error creating reminder: {e}")
            return None

    @classmethod
    @sync_to_async
    def get_pending_reminder(cls, current_time):

        reminders_due = Reminder.objects.filter(reminder_date_time__lte=current_time, status=StatusChoices.PENDING)
        for reminder in reminders_due:
            user = reminder.user.telegram_id
            text = reminder.text
            return user, text

    @classmethod
    @sync_to_async
    def change_status(cls, user):
        reminder = Reminder.objects.filter(user__telegram_id=user)
        reminder.update(status=StatusChoices.SENT)
