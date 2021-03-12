from django.contrib import admin

from bot_API import models


@admin.register(models.BotPlatform)
class BotPlatformAdmin(admin.ModelAdmin):
    list_display = ('platform', 'description')
    search_fields = ('platform', 'description')
    ordering = ['platform']


@admin.register(models.BotInfo)
class BotInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform')
    search_fields = ('title', 'platform')
    ordering = ['-update_date']
