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


class BotInfo(models.Model):
    title = models.CharField(max_length=80, verbose_name='Название')
    platform = models.OneToOneField(BotPlatform, verbose_name='Платформа', on_delete=models.PROTECT)
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
