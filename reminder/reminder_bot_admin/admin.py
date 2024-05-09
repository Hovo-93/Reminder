from django.contrib import admin
from reminder_bot_admin.models import *


class ReminderInline(admin.StackedInline):
    model = Reminder
    extra = 0


class ReminderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reminder._meta.fields]
    list_filter = ['user']


class TgUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TelegramUser._meta.fields]
    inlines = [ReminderInline]


admin.site.register(TelegramUser, TgUserAdmin)
admin.site.register(Reminder, ReminderAdmin)
