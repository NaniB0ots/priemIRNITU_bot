from django.contrib import admin

from vk_bot import models


@admin.register(models.VkUser)
class VkUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'name', 'phone_number')
    search_fields = ('chat_id', 'name', 'phone_number')
    ordering = ['-update_date']
