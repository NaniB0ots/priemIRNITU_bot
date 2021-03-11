from django.contrib import admin

from tg_bot import models


@admin.register(models.TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'name', 'phone_number')
    search_fields = ('chat_id', 'name', 'phone_number')
    ordering = ['-update_date']
