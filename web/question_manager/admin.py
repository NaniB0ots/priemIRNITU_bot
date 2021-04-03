from django.contrib import admin

from question_manager import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'parent_category', 'editor', 'contains_questions')
    search_fields = ('category',)
    list_filter = ('contains_questions',)
    ordering = ['-update_date']


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'category', 'editor')
    search_fields = ('question', 'answer')
    list_filter = ('category',)
    ordering = ['-update_date']
