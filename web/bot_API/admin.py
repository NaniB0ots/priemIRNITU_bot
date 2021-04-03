from django.contrib import admin

from bot_API import models


@admin.register(models.BotCommands)
class BotCommandsAdmin(admin.ModelAdmin):
    list_display = ('command_type', 'message')
    search_fields = ('command_type', 'message')
    ordering = ['-update_date']
