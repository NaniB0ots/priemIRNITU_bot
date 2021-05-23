import traceback

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline, TrigramSimilarity
from django.db.models import Value

from bot_API import models
from project.logger import logger
from question_manager import models as question_manager_models
from request_manager import models as request_manager_models


class ChatBotActions:
    model = models.BotCommands
    default_message = 'Скоро здесь будет что-то интересное 😉'

    def get_start_message(self) -> str:
        try:
            message = self.model.objects.get(command_type='start').message
        except self.model.DoesNotExist:
            message = 'Привет!'
        return message

    def get_help_message(self) -> str:
        try:
            message = self.model.objects.get(command_type='help').message
        except self.model.DoesNotExist:
            message = self.default_message
        return message

    def get_about_message(self) -> str:
        try:
            message = self.model.objects.get(command_type='about').message
        except self.model.DoesNotExist:
            message = self.default_message
        return message

    @staticmethod
    def get_error_text() -> str:
        text = 'Что-то пошло не так... Попробуйте ещё раз'
        return text

    @staticmethod
    def get_invalid_text_answer() -> str:
        text = 'Я Вас не понимаю. Воспользуйтесь клавиатурой'
        return text


class CategoriesManager:
    model = question_manager_models.Category

    def get_categories(self,
                       parent_category: question_manager_models.Category = None,
                       parent_category_text: str = None):
        if parent_category_text:
            try:
                parent_category = self.model.objects.get(category=parent_category_text)
            except self.model.DoesNotExist:
                return self.model.objects.none()

        if parent_category:
            try:
                categories = self.model.objects.filter(parent=parent_category)
            except self.model.DoesNotExist:
                return self.model.objects.none()
        else:
            try:
                categories = self.model.objects.filter(parent=None)
            except self.model.DoesNotExist:
                return self.model.objects.none()

        return categories


class QuestionsManager:
    model = question_manager_models.Question
    category_model = question_manager_models.Category

    def get_category_category_text(self, category_text):
        try:
            return self.category_model.objects.get(category=category_text)
        except self.category_model.DoesNotExist:
            return self.model.objects.none()

    def get_questions(self,
                      category: question_manager_models.Category = None,
                      category_text: str = None):
        if category_text:
            category = self.get_category_category_text(category_text)

        if category:
            try:
                questions = self.model.objects.filter(category=category)
            except self.model.DoesNotExist:
                return self.model.objects.none()
        else:
            return self.model.objects.none()

        return questions

    def get_answer(self, category_text: str):
        category = self.get_category_category_text(category_text)
        if category:
            try:
                return self.model.objects.get(category).answer
            except self.model.DoesNotExist:
                self.model.objects.none()
        else:
            self.model.objects.none()

    @classmethod
    def search(cls, search_text):
        try:
            result = cls.model.objects.annotate(similarity=TrigramSimilarity('question', search_text)
                                                ).filter(similarity__gt=0.3).order_by('-similarity')
            logger.debug(f'Найдено в поиске: {result.count()}')
        except:
            logger.error(traceback.format_exc())
            result = cls.model.objects.none()
        return result


class RequestManager:
    request_model = request_manager_models.RequestHistory
    search_model = request_manager_models.SearchHistory

    @classmethod
    def create_request(cls, phone_number: str, question: str):
        """
        Создание запроса обратной связи.
        :param phone_number:
        :param question:
        :return:
        """
        cls.request_model.objects.create(phone_number=phone_number,
                                         question=question,
                                         status='Ожидает')

    @classmethod
    def create_question(cls, question: str):
        """
        Сохранение результата поиска
        :param question:
        :return:
        """
        cls.search_model.objects.create(question=question)
