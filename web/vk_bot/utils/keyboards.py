from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from question_manager import models as question_manager_models


def get_main_menu_keyboard() -> VkKeyboard:
    keyboard = VkKeyboard()

    keyboard.add_button('Частые вопросы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Заказать звонок', color=VkKeyboardColor.SECONDARY)

    return keyboard


def get_categories_keyboard(categories: question_manager_models.Category.objects) -> VkKeyboard:
    keyboard = VkKeyboard()

    for category in categories:
        keyboard.add_button(category.category, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

    keyboard.add_button('Основное меню', color=VkKeyboardColor.SECONDARY)
    return keyboard
