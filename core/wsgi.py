import os

from django.core.wsgi import get_wsgi_application
from threading import Thread
from tg_bot.tg_bot import bot as tg_bot
from vk_bot.vk_bot import bot as vk_bot

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# запуск чат-ботов
thread_tg = Thread(target=tg_bot.infinity_polling)
thread_tg.start()
thread_vk = Thread(target=vk_bot.run_forever)
thread_vk.start()


application = get_wsgi_application()
