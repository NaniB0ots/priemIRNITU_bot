from django.db import models

from web.project.settings import BOT_PLATFORMS


class BotInfo(models.Model):
    title = models.CharField(max_length=80, verbose_name='Название')
    platform = models.CharField(max_length=80, choices=BOT_PLATFORMS, verbose_name='Платформа')
    url = models.URLField(blank=True, verbose_name='Ссылка на бота')
    start_message = models.TextField(blank=True, verbose_name='Стартовое сообщение')
    help_message = models.TextField(blank=True, verbose_name='Сообщение с помощью')
    about_message = models.TextField(blank=True, verbose_name='Описание чат-бота')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Чат-бот'
        verbose_name_plural = 'Чат-боты'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'
