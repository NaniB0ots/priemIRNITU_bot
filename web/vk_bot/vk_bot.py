import random
import time

import vk_api
from vk_api.keyboard import VkKeyboard
from vk_api.longpoll import VkLongPoll, VkEventType

from bot_API.utils.PhoneNumberValidator import is_valid_phone_number

from bot_API import core
from bot_API.core import ChatBotActions
from project.logger import logger
from project.settings import VK_TOKEN
from vk_bot.utils import keyboards
from vk_bot import models

if not VK_TOKEN:
    raise ValueError('VK_TOKEN не может быть пустым')


class NextStep:
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs


class VkBot(ChatBotActions):
    def __init__(self, token):
        self.vk = vk_api.VkApi(token=token)
        self.long_poll = VkLongPoll(self.vk)
        self.user: models.VkUser = models.VkUser.objects.none()
        self.next_step_users: {str: NextStep} = {}

    def send_message(self, user_id: int, text, keyboard: VkKeyboard = None):
        """
        Отправка сообщения пользователю.
        :param user_id:
        :param text:
        :param keyboard:
        :return:
        """

        values = {
            'user_id': user_id,
            'message': text,
            'random_id': random.randint(0, 2048)
        }

        if keyboard:
            values['keyboard'] = keyboard.get_keyboard(),
        self.vk.method('messages.send', values)

    def polling(self):
        """
        Получение обновлений от Вк.
        :return:
        """
        logger.info('Вк бот запущен...')
        for event in self.long_poll.listen():
            self.event_handling(event)

    def infinity_polling(self):
        """
        Получение обновлений от Вк без остановки.
        :return:
        """
        while True:
            try:
                self.polling()
            except Exception as e:
                time.sleep(1)
                continue

    def get_user(self, event) -> models.VkUser:
        """
        Получение или создание пользователя из базы данных.
        :param event:
        :return:
        """
        user = self.vk.method("users.get", {"user_ids": event.user_id})
        fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
        try:
            user_object = models.VkUser.objects.get(chat_id=event.user_id)
        except models.VkUser.DoesNotExist:
            user_object = models.VkUser.objects.create(chat_id=event.user_id, name=fullname)
        self.user = user_object
        return self.user

    def register_next_step_by_user_id(self, user_id, callback, *args, **kwargs):
        """
        Регистрация функции, которая обработает слдующий ивент по user_id.
        :param user_id:
        :param callback:
        :param args:
        :param kwargs:
        :return:
        """
        next_step = NextStep(callback, *args, **kwargs)
        self.next_step_users[user_id] = next_step

    def register_next_step(self, event, callback, *args, **kwargs):
        """
        Регистрация функции, которая обработает слдующий ивент.
        :param event:
        :param callback:
        :param args:
        :param kwargs:
        :return:
        """
        user_id = event.user_id
        self.register_next_step_by_user_id(user_id, callback, *args, **kwargs)

    def processing_next_step(self, event):
        """
        Обработка запланированных ивентов.
        :param event:
        :return:
        """
        user_id = event.user_id
        if self.next_step_users.get(user_id):
            next_step = self.next_step_users[user_id]
            del self.next_step_users[user_id]
            next_step.callback(event, *next_step.args, **next_step.kwargs)
            return True

    def event_handling(self, event):
        """
        Обработка событий бота.
        :param event:
        :return:
        """
        if event.to_me:
            self.get_user(event)
            if self.processing_next_step(event):
                return
            elif event.type == VkEventType.MESSAGE_NEW:
                self.message_processing(event)

    def write_phone_number_step(self, event):
        """
        Получение номера телефона пользователя.
        :param event:
        :return:
        """
        if event.text.lower() == 'отмена':
            text = 'Тогда в другой раз😊'
            self.send_message(user_id=event.user_id, text=text, keyboard=keyboards.get_main_menu_keyboard())
            return
        text = 'Скоро мы с вами свяжемся😉\n' \
               'Спасибо!'
        phone_number = event.text
        if is_valid_phone_number(phone_number):
            # сохраняем номер телефона
            self.user.phone_number = phone_number
            self.user.save()

            core.RequestManager.create_request(phone_number=phone_number, question=self.user.last_question)

            self.send_message(user_id=event.user_id, text=text, keyboard=keyboards.get_main_menu_keyboard())
        else:
            self.send_message(user_id=event.user_id, text='Вы ввели некорректный номер телефона😨\n'
                                                          'Попробуйте ещё раз😌', )
            self.register_next_step(event, self.write_phone_number_step)

    def ask_question_step(self, event):
        """
        Получение вопроса пользователя для обратной связи.
        :param event:
        :return:
        """
        if event.text.lower() == 'отмена':
            text = 'Тогда в другой раз😊'
            self.send_message(user_id=event.user_id, text=text, keyboard=keyboards.get_main_menu_keyboard())
            return

        # сохраняем вопрос
        self.user.last_question = event.text
        self.user.save()

        text = 'Отлично!\n' \
               'А теперь введите номер телефона'
        self.send_message(user_id=event.user_id, text=text)
        self.register_next_step(event, self.write_phone_number_step)

    def message_processing(self, event):
        """
        Обработка текстовых сообщений.
        :param event:
        :return:
        """
        categories_manager = core.CategoriesManager()
        user_id = event.user_id
        event_text = event.text

        if event_text == 'Начать':
            text = self.get_start_message()
            self.send_message(user_id=user_id, text=text, keyboard=keyboards.get_main_menu_keyboard())

        elif event_text == 'Основное меню':
            text = 'Основное меню'
            self.send_message(user_id=user_id, text=text, keyboard=keyboards.get_main_menu_keyboard())

        elif event.text.lower() == 'отмена':
            text = 'Тогда в другой раз😊'
            self.send_message(user_id=event.user_id, text=text, keyboard=keyboards.get_main_menu_keyboard())
            return

        elif event_text == 'Заказать звонок':
            text = 'Введите ваш вопрос'
            self.send_message(user_id=user_id, text=text, keyboard=keyboards.get_cancel_keyboard())

            self.register_next_step(event, self.ask_question_step)

        elif 'Частые вопросы' in event_text:
            categories = categories_manager.get_categories()
            text = 'Категории'
            self.send_message(user_id=user_id, text=text,
                              keyboard=keyboards.get_categories_keyboard(categories))

        else:
            if '« ' in event_text:
                event_text = event_text[2:]
            elif '<<' in event_text:
                event_text = event_text[3:]

            categories = categories_manager.get_categories(parent_category_text=event_text)
            if categories:
                text = 'Категории'
                self.send_message(user_id=user_id, text=text,
                                  keyboard=keyboards.get_categories_keyboard(categories))
                return

            questions_manager = core.QuestionsManager()
            questions = questions_manager.get_questions(category_text=event_text)
            if questions:
                for question in questions:
                    text = f'❓Вопрос:\n' \
                           f'{question.question}\n\n' \
                           f'❗Ответ:\n' \
                           f'{question.answer}'
                    self.send_message(user_id=user_id, text=text)
                return

            else:
                text = bot.get_invalid_text_answer()
                self.send_message(user_id=user_id, text=text, keyboard=keyboards.get_main_menu_keyboard())
                return


bot = VkBot(VK_TOKEN)
