from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from question_manager import models


class QuestionInline(admin.TabularInline):
    model = models.Question
    show_change_link = True
    extra = 0


@admin.register(models.Category)
class CategoryAdmin(DraggableMPTTAdmin):
    inlines = [
        QuestionInline,
    ]
    mptt_level_indent = 30
    list_display = ('tree_actions', 'indented_title',)
    list_display_links = ('indented_title',)

    def get_object(self, *args, **kwargs):
        category = super(CategoryAdmin, self).get_object(*args, **kwargs)
        # Если у категории есть подкатегории убираем вложенные сообщения.
        if models.Category.objects.filter(parent=category):
            self.inlines = []
        else:
            self.inlines = [QuestionInline]
        return category

    class Media:
        css = {
            'all': ('css/admin/custom_admin.css',)
        }


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'category')
    search_fields = ('question', 'answer')
    list_filter = ('category',)
    ordering = ['-update_date']
