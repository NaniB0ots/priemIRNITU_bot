from telebot import types
from question_manager import models as question_manager_models


MAX_CALLBACK_RANGE = 41


def get_main_menu_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton('Частые вопросы')
    btn2 = types.KeyboardButton('Заказать звонок')
    btn3 = types.KeyboardButton('Поиск')

    markup.add(btn1)
    markup.add(btn2, btn3)
    return markup


def get_cancel_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton('Отмена')

    markup.add(btn1)
    return markup


def get_categories_keyboard(categories: question_manager_models.Category.objects):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)

    for category in categories:
        btn1 = types.KeyboardButton(category.category)
        markup.add(btn1)

    if categories and categories[0].parent:
        if not categories[0].parent.parent:
            text = f'<< Частые вопросы'
        else:
            text = f'<< {categories[0].parent.parent}'
        btn = types.KeyboardButton(text)
        markup.add(btn)

    btn2 = types.KeyboardButton('Основное меню')
    markup.add(btn2)
    return markup


def get_question_not_found_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton('Частые вопросы')
    btn2 = types.KeyboardButton('Заказать звонок')
    btn3 = types.KeyboardButton('Основное меню')

    markup.add(btn1, btn2)
    markup.add(btn3)
    return markup
