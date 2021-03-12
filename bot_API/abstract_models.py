from django.db import models

from bot_API.models import BotPlatform


class BotInfo(models.Model):
    title = models.CharField(max_length=80, verbose_name='Название')
    platform = models.ForeignKey(BotPlatform, verbose_name='Платформа', on_delete=models.PROTECT)
    url = models.URLField(blank=True, verbose_name='Ссылка на бота')
    start_message = models.TextField(blank=True, verbose_name='Стартовое сообщение')
    help_message = models.TextField(blank=True, verbose_name='Сообщение с помощью')
    about_message = models.TextField(blank=True, verbose_name='Описание чат-бота')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
