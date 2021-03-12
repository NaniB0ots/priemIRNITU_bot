import os

from django.core.wsgi import get_wsgi_application
from threading import Thread
from tg_bot.tg_bot import bot

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# запуск чат-ботов
thread_tg = Thread(target=bot.infinity_polling)
thread_tg.start()

application = get_wsgi_application()
