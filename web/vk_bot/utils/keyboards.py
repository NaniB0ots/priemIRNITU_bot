from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_main_menu_keyboard() -> VkKeyboard:
    keyboard = VkKeyboard()

    keyboard.add_button('Частые вопросы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Заказать звонок', color=VkKeyboardColor.SECONDARY)

    return keyboard
