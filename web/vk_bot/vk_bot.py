import random
import time

import vk_api
from vk_api.keyboard import VkKeyboard
from vk_api.longpoll import VkLongPoll, VkEventType

from bot_API import core
from bot_API.core import ChatBotActions
from project.settings import VK_TOKEN
from vk_bot.utils import keyboards

if not VK_TOKEN:
    raise ValueError('VK_TOKEN не может быть пустым')


class VkBot(ChatBotActions):
    def __init__(self, token):
        self.vk = vk_api.VkApi(token=token)
        self.long_poll = VkLongPoll(self.vk)

    def send_message(self, user_id: int, text, keyboard: VkKeyboard = None):

        values = {
            'user_id': user_id,
            'message': text,
            'random_id': random.randint(0, 2048)
        }

        if keyboard:
            values['keyboard'] = keyboard.get_keyboard(),
        self.vk.method('messages.send', values)

    def polling(self):
        print('Vk бот запущен...')
        for event in self.long_poll.listen():
            self.event_handling(event)

    def infinity_polling(self):
        while True:
            try:
                self.polling()
            except Exception as e:
                time.sleep(3)
                continue

    def event_handling(self, event):
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                self.message_processing(event)

    def message_processing(self, event):
        categories_manager = core.CategoriesManager()
        user_id = event.user_id
        if event.text == 'Начать':
            text = self.get_start_message()
            self.send_message(user_id=user_id, text=text, keyboard=keyboards.get_main_menu_keyboard())

        elif event.text == 'Основное меню':
            text = 'Основное меню'
            self.send_message(user_id=user_id, text=text, keyboard=keyboards.get_main_menu_keyboard())

        elif event.text == 'Частые вопросы':
            categories = categories_manager.get_categories()
            text = 'Категории'
            self.send_message(user_id=user_id, text=text,
                              keyboard=keyboards.get_categories_keyboard(categories))

        else:
            categories = categories_manager.get_categories(parent_category_text=event.text)
            if categories:
                text = 'Категории'
                self.send_message(user_id=user_id, text=text,
                                  keyboard=keyboards.get_categories_keyboard(categories))
                return

            questions_manager = core.QuestionsManager()
            questions = questions_manager.get_questions(category_text=event.text)
            if questions:
                for question in questions:
                    text = f'Вопрос:\n' \
                           f'{question.question}\n\n' \
                           f'Ответ:\n' \
                           f'{question.answer}'
                    self.send_message(user_id=user_id, text=text)
                return

            else:
                text = bot.get_invalid_text_answer()
                self.send_message(user_id=user_id, text=text, keyboard=keyboards.get_main_menu_keyboard())
                return


bot = VkBot(VK_TOKEN)
