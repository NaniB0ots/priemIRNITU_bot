from django.contrib import admin

from question_manager import models


@admin.register(models.Category)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('category', 'parent_category_id', 'editor', 'contains_questions')
    search_fields = ('category',)
    list_filter = ('contains_questions',)
    ordering = ['-update_date']
