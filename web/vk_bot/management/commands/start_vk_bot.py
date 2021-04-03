from django.core.management.base import BaseCommand

from project.settings import DEBUG
from vk_bot.vk_bot import bot


class Command(BaseCommand):
    help = 'Запуск Вк бота'

    def handle(self, *args, **options):
        if DEBUG:
            bot.polling()
        else:
            bot.infinity_polling()
