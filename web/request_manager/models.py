from django.contrib.auth.models import User
from django.db import models

from tg_bot.models import TelegramUser
from vk_bot.models import VkUser


class RequestStatus(models.Model):
    status = models.CharField(max_length=100, verbose_name='Статус')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Статус запроса обратной связи'
        verbose_name_plural = 'Статусы запроса обратной связи'
        ordering = ['-update_date']

    def __str__(self):
        return f'{self.status}'


class RequestHistory(models.Model):
    editor = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                               verbose_name='Кто изменил')
    status = models.ForeignKey(RequestStatus, on_delete=models.DO_NOTHING, verbose_name='Статус')
    tg_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name='Пользователь telegram')
    vk_user = models.ForeignKey(VkUser, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name='Пользователь Вконтакте')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Запрос обратной связи'
        verbose_name_plural = 'Запросы обратной связи'
        ordering = ['-update_date']

    def __str__(self):
        return f'{self.status} {self.editor}'
