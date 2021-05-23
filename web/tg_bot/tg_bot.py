import telebot

from bot_API import core
from bot_API.core import ChatBotActions
from project.logger import logger
from project.settings import TG_TOKEN

from tg_bot.utils import keyboards
from bot_API.utils.PhoneNumberValidator import is_valid_phone_number
from tg_bot import models

if not TG_TOKEN:
    raise ValueError('TG_TOKEN не может быть пустым')


class TelegramBot(telebot.TeleBot, ChatBotActions):
    def infinity_polling(self, *args, **kwargs):
        logger.info('Telegram бот запущен...')
        super(TelegramBot, self).infinity_polling(*args, **kwargs)


bot = TelegramBot(TG_TOKEN)
categories_manager = core.CategoriesManager()
questions_manager = core.QuestionsManager()


# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    user = models.TelegramUser.objects.get_or_create(chat_id=chat_id)[0]
    if message.from_user.first_name:
        user.name = message.from_user.first_name
    user.username = message.from_user.username
    user.save()
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
    user = models.TelegramUser.objects.get_or_create(chat_id=chat_id)[0]
    if message.from_user.first_name:
        user.name = message.from_user.first_name
    user.username = message.from_user.username
    user.save()
    message_to_send = 'Введите интересующий Вас вопрос'
    msg = bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_cancel_keyboard())
    bot.register_next_step_handler(msg, feedback_processing)


def feedback_processing(message):
    chat_id = message.chat.id
    user = models.TelegramUser.objects.get_or_create(chat_id=chat_id)[0]

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
    user = models.TelegramUser.objects.get_or_create(chat_id=chat_id)[0]

    if message.text == 'Отмена':
        message_to_send = 'Тогда в другой раз😊'
        bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_main_menu_keyboard())
    else:
        phone_number = message.text
        if is_valid_phone_number(phone_number):
            core.RequestManager.create_request(phone_number=phone_number, question=user.last_question)
            user.phone_number = phone_number
            user.save()
            message_to_send = 'Заявка принята! Мы Вам перезвоним😊'
            bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_main_menu_keyboard())

        else:
            message_to_send = 'Вы ввели некорректный номер телефона, попробуйте еще раз'
            msg = bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_cancel_keyboard())
            bot.register_next_step_handler(msg, phone_number_processing)


@bot.message_handler(regexp='^Частые вопросы$|^<< Частые вопросы$')
def message(message):
    chat_id = message.chat.id
    user = models.TelegramUser.objects.get_or_create(chat_id=chat_id)[0]
    if message.from_user.first_name:
        user.name = message.from_user.first_name
    user.username = message.from_user.username
    user.save()
    message_to_send = 'Выберите инетресующую Вас категорию'
    categories = categories_manager.get_categories()
    bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_categories_keyboard(categories))


@bot.message_handler(regexp='Поиск')
def message(message):
    chat_id = message.chat.id
    user = models.TelegramUser.objects.get_or_create(chat_id=chat_id)[0]
    if message.from_user.first_name:
        user.name = message.from_user.first_name
    user.username = message.from_user.username
    user.save()
    message_to_send = 'Введите интересующий Вас вопрос'
    msg = bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_cancel_keyboard())
    bot.register_next_step_handler(msg, search_processing)


def search_processing(message):
    chat_id = message.chat.id
    if message.text == 'Отмена':
        message_to_send = 'Тогда в другой раз😊'
        bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_main_menu_keyboard())
    else:
        questions = core.QuestionsManager.search(message.text)
        if not questions:
            core.RequestManager.create_question(question=message.text)
            message_to_send = 'На данный момент, интересующего вопроса нет в нашей базе😔\n' \
                              'Но не беспокойтесь, мы его записали и в ближайшее время добавим в бота🤓\n' \
                              'Желаете оставить запрос на обратный звонок или поискать информацию в часто ' \
                              'задаваемых вопросах?'
            bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_question_not_found_keyboard())
            return
        else:
            message_to_send = 'Результат поиска😉'
            bot.send_message(chat_id=chat_id, text=message_to_send, reply_markup=keyboards.get_main_menu_keyboard())
            for question in questions:
                message_to_send = f'❓Вопрос:\n' \
                                  f'{question.question}\n\n' \
                                  f'❗Ответ:\n' \
                                  f'{question.answer}'
                bot.send_message(chat_id=chat_id, text=message_to_send)
            return


@bot.message_handler(content_types=['text'])
def message(message):
    chat_id = message.chat.id
    text = message.text

    if "<<" in text:
        text = text[3:]

    categories = categories_manager.get_categories(parent_category_text=text)
    if categories:
        chat_id = message.chat.id
        message_to_send = 'Выберите инетресующую Вас категорию'
        bot.send_message(chat_id=chat_id, text=message_to_send,
                         reply_markup=keyboards.get_categories_keyboard(categories))
        return
    questions = questions_manager.get_questions(category_text=text)
    if questions:
        for question in questions:
            text = f'❓Вопрос:\n' \
                   f'{question.question}\n\n' \
                   f'❗Ответ:\n' \
                   f'{question.answer}'
            bot.send_message(chat_id=chat_id, text=text)
        return
    else:
        message_to_send = bot.get_invalid_text_answer()
        bot.send_message(chat_id=chat_id, text=message_to_send,
                         reply_markup=keyboards.get_main_menu_keyboard())
        return
