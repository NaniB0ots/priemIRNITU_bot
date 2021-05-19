from django.db import models


class TelegramUser(models.Model):
    chat_id = models.CharField(max_length=15, verbose_name='chat_id')
    name = models.CharField(max_length=150, verbose_name='Имя', blank=True)
    phone_number = models.CharField(max_length=150, verbose_name='Номер телефона', blank=True)
    last_question = models.TextField(verbose_name='Последний заданный вопрос', blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пользователь telegram'
        verbose_name_plural = 'Пользователи telegram'
        ordering = ['-update_date']

    def __str__(self):
        return f'{self.chat_id}'
