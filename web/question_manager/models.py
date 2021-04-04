from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    category = models.CharField(max_length=37, unique=True, verbose_name='Категория')

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='children', verbose_name='Родительская категория')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ['category']

    def __str__(self):
        return f'{self.category}'


class Question(models.Model):
    category = TreeForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-update_date']

    def __str__(self):
        return f'{self.question}'
