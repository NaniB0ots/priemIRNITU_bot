import telebot

from bot_API import core
from bot_API.core import ChatBotActions
from project.settings import TG_TOKEN

from tg_bot.utils import keyboards
from bot_API.utils.PhoneNumberValidator import is_valid_phone_number
from tg_bot import models

if not TG_TOKEN:
    raise ValueError('TG_TOKEN не может быть пустым')


class TelegramBot(telebot.TeleBot, ChatBotActions):
    def infinity_polling(self, *args, **kwargs):
        print('Telegram бот запущен...')
        super(TelegramBot, self).infinity_polling(*args, **kwargs)


bot = TelegramBot(TG_TOKEN)
user = models.TelegramUser.objects.none()

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    message_to_send = bot.get_start_message()
    bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_main_menu_keyboard())


@bot.message_handler(commands=['help'])
def help_message(message):
    chat_id = message.chat.id
    message_to_send = bot.get_help_message()
    bot.send_message(chat_id=chat_id, text=message_to_send)


@bot.message_handler(regexp='^Основное меню$|^Отмена$')
def message(message):
    chat_id = message.chat.id
    if message.text == 'Отмена':
        message_to_send = 'Тогда в другой раз😊'
    else:
        message_to_send = message.text
    bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_main_menu_keyboard())


@bot.message_handler(regexp='^Заказать звонок$')
def message(message):
    chat_id = message.chat.id
    message_to_send = 'Введите интересующий Вас вопрос'
    msg = bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_cancel_keyboard())
    bot.register_next_step_handler(msg, feedback_processing)


def feedback_processing(message):
    chat_id = message.chat.id

    if message.text == 'Отмена':
        message_to_send = 'Тогда в другой раз😊'
        bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_main_menu_keyboard())
    else:
        user.last_question = message.text
        message_to_send = 'Введите Ваш номер телефона'
        msg = bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_cancel_keyboard())
        bot.register_next_step_handler(msg, phone_number_processing)



def phone_number_processing(message):
    chat_id = message.chat.id

    if message.text == 'Отмена':
        message_to_send = 'Тогда в другой раз😊'
        bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_main_menu_keyboard())
    else:
        phone_number = message.text
        print(f'Номер телефона: {phone_number}')
        if is_valid_phone_number(phone_number):
            core.RequestManager.create_request(phone_number=phone_number, question=user.last_question)
            message_to_send = 'Заявка принята! Мы Вам перезвоним😊'
            bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_main_menu_keyboard())

        else:
            message_to_send = 'Вы ввели некорректный номер телефона, попробуйте еще раз'
            msg = bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_cancel_keyboard())
            bot.register_next_step_handler(msg, phone_number_processing)


@bot.message_handler(regexp=['^Частые вопросы$'])
def message(message):
    chat_id = message.chat.id

    pass


@bot.message_handler(commands=['Поиск'])
def message(message):
    chat_id = message.chat.id

    pass