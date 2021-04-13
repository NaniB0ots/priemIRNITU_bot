from django.contrib import admin

from request_manager import models


@admin.register(models.RequestHistory)
class RequestHistoryAdmin(admin.ModelAdmin):
    list_display = ('status', 'creation_date', 'phone_number', 'question', 'editor',)
    search_fields = ('editor', 'phone_number', 'question')
    list_filter = ('status',)
    ordering = ['-status', '-update_date']
    exclude = ('editor',)

    readonly_fields = ('phone_number', 'question',)

    def save_model(self, request, obj, form, change):
        obj.editor = request.user  # добавляем текущего пользователя в editor
        super(RequestHistoryAdmin, self).save_model(request, obj, form, change)
