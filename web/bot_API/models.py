from django.db import models

from project.settings import COMMAND_TYPES


class BotCommands(models.Model):
    command_type = models.TextField(max_length=150, choices=COMMAND_TYPES, unique=True,
                                    verbose_name='Тип команды')
    message = models.TextField(verbose_name='Сообщение')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Команду бота'
        verbose_name_plural = 'Команды бота'
        ordering = ['-update_date']

    def __str__(self):
        return f'{self.message}'
