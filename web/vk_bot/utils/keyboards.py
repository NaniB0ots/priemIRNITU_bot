from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from question_manager import models as question_manager_models


def get_main_menu_keyboard() -> VkKeyboard:
    keyboard = VkKeyboard()

    keyboard.add_button('Частые вопросы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Заказать звонок')
    keyboard.add_button('Поиск')

    return keyboard


def get_categories_keyboard(categories: question_manager_models.Category.objects) -> VkKeyboard:
    keyboard = VkKeyboard()

    for category in categories:
        keyboard.add_button(category.category, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

    if categories and categories[0].parent:
        if not categories[0].parent.parent:
            text = f'<< Частые вопросы'
        else:
            text = f'<< {categories[0].parent.parent}'
        keyboard.add_button(text, color=VkKeyboardColor.SECONDARY)
        keyboard.add_line()

    keyboard.add_button('Основное меню', color=VkKeyboardColor.SECONDARY)
    return keyboard


def get_cancel_keyboard() -> VkKeyboard:
    keyboard = VkKeyboard()
    keyboard.add_button('Отмена', color=VkKeyboardColor.SECONDARY)
    return keyboard


def get_question_not_found_keyboard():
    keyboard = VkKeyboard()
    keyboard.add_button('Частые вопросы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Заказать звонок', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Основное меню')

    return keyboard
