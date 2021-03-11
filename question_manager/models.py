from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Категория')
    parent_category_id = models.IntegerField(null=True, blank=True, verbose_name='Id родительской категории')
    editor = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Кто изменил')
    contains_questions = models.BooleanField(default=True, verbose_name='Содержит вопросы (иначе категории)')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-update_date']

    def __str__(self):
        return f'{self.category}'


class Question(models.Model):
    question = models.CharField(max_length=100, verbose_name='Вопрос')
    answer = models.CharField(max_length=195, verbose_name='Ответ')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    editor = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Кто изменил')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-update_date']

    def __str__(self):
        return f'{self.question}'
