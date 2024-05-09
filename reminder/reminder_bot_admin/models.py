from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class TelegramUser(models.Model):
    telegram_id = models.PositiveIntegerField(unique=True, null=True, blank=True)
    name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Ник в телеграм"
    )
    full_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Имя-Фамилия"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"@{self.name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class StatusChoices(models.TextChoices):
    PENDING = "parsed", _("Ожидание")
    SENT = "sent", _("Отправлено")
    FAILED = "failed", _("Ошибка")


class Reminder(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='reminders')
    text = models.CharField(max_length=500)
    reminder_date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=StatusChoices, default=StatusChoices.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Напоминание"
        verbose_name_plural = "Напоминания"
