from django.contrib import admin

from request_manager import models


@admin.register(models.RequestStatus)
class RequestStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
    ordering = ['-update_date']


@admin.register(models.RequestHistory)
class RequestHistoryAdmin(admin.ModelAdmin):
    list_display = ('status', 'editor', 'tg_user', 'vk_user')
    search_fields = ('editor', 'tg_user', 'vk_user')
    ordering = ['-update_date']

    exclude = ('tg_user', 'vk_user',)

    def get_fieldsets(self, *args, **kwargs):
        fieldsets = super(RequestHistoryAdmin, self).get_fieldsets(*args, **kwargs)
        print(fieldsets)
        return fieldsets
