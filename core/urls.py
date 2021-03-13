from django.contrib import admin
from django.urls import path
from threading import Thread
from vk_bot.vk_bot import bot as vk_bot

urlpatterns = [
    path('admin/', admin.site.urls),
]

# запуск чат-ботов
# thread_vk = Thread(target=vk_bot.run_forever)
# thread_vk.start()
