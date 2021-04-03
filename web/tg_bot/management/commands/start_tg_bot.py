from django.core.management.base import BaseCommand

from tg_bot import bot


class Command(BaseCommand):
    help = 'Запуск телеграм бота'

    def handle(self, *args, **options):
        bot.infinity_polling()
