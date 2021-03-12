from django.db import models


class BotPlatform(models.Model):
    platform = models.CharField(max_length=60, verbose_name='Название платформы')
    create_bot_url = models.URLField(blank=True, verbose_name='Ссылка на создание бота')
    description = models.TextField(blank=True, verbose_name='Инструкция по созданию бота')

    class Meta:
        verbose_name = 'Платформа чат-бота'
        verbose_name_plural = 'Платформы чат-ботов'
        ordering = ['platform']

    def __str__(self):
        return f'{self.platform}'
