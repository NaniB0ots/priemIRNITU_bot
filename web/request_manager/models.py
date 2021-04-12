from django.contrib.auth.models import User
from django.db import models

from tg_bot.models import TelegramUser
from vk_bot.models import VkUser


class RequestHistory(models.Model):
    editor = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                               verbose_name='Кто изменил')

    status = models.CharField(max_length=150, choices=[('Отвечено', 'Отвечено'), ('Ожидает', 'Ожидает')],
                              verbose_name='Статус')

    phone_number = models.CharField(max_length=150, verbose_name='Номер телефона')
    question = models.TextField(verbose_name='Вопрос')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Запрос обратной связи'
        verbose_name_plural = 'Запросы обратной связи'
        ordering = ['-update_date']

    def __str__(self):
        return f'{self.status} {self.editor}'
