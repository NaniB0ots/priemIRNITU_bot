import telebot

from bot_API.core import ChatBotActions
from project.settings import TG_TOKEN

if not TG_TOKEN:
    raise ValueError('TG_TOKEN не может быть пустым')


class TelegramBot(telebot.TeleBot, ChatBotActions):
    platform = 'tg'

    def infinity_polling(self, *args, **kwargs):
        self.check_platform()
        print('Telegram бот запущен...')
        super(TelegramBot, self).infinity_polling(*args, **kwargs)


bot = TelegramBot(TG_TOKEN)


# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    message = bot.get_start_message()
    bot.send_message(chat_id=chat_id, text=message)
