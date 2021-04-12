from django.contrib import admin

from request_manager import models


@admin.register(models.RequestHistory)
class RequestHistoryAdmin(admin.ModelAdmin):
    list_display = ('status', 'editor', 'phone_number', 'question')
    search_fields = ('editor', 'phone_number', 'question')
    list_filter = ('status',)
    ordering = ['-update_date']

    def get_fieldsets(self, *args, **kwargs):
        fieldsets = super(RequestHistoryAdmin, self).get_fieldsets(*args, **kwargs)
        print(fieldsets)
        return fieldsets
