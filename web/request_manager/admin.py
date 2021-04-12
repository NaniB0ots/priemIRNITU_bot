from django.contrib import admin

from request_manager import models


@admin.register(models.RequestHistory)
class RequestHistoryAdmin(admin.ModelAdmin):
    list_display = ('status', 'editor', 'phone_number', 'question')
    search_fields = ('editor', 'phone_number', 'question')
    list_filter = ('status',)
    ordering = ['status', '-update_date']
    exclude = ('editor',)

    readonly_fields = ('phone_number', 'question',)
