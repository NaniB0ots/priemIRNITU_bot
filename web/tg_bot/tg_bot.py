import telebot

from bot_API.core import ChatBotActions
from project.settings import TG_TOKEN

if not TG_TOKEN:
    raise ValueError('TG_TOKEN не может быть пустым')


class TelegramBot(telebot.TeleBot, ChatBotActions):
    def infinity_polling(self, *args, **kwargs):
        print('Telegram бот запущен...')
        super(TelegramBot, self).infinity_polling(*args, **kwargs)


bot = TelegramBot(TG_TOKEN)


# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    message = bot.get_start_message()
    bot.send_message(chat_id=chat_id, text=message)


@bot.message_handler(commands=['help'])
def help_message(message):
    chat_id = message.chat.id
    message = bot.get_help_message()
    bot.send_message(chat_id=chat_id, text=message)
