from telebot import types
import json

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

