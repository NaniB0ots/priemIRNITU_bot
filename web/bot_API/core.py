from bot_API import models
from question_manager import models as question_manager_models


class ChatBotActions:
    model = models.BotCommands
    default_message = 'Скоро здесь будет что-то интересное 😉'

    def get_start_message(self):
        try:
            message = self.model.objects.get(command_type='start').message
        except self.model.DoesNotExist:
            message = 'Привет!'
        return message

    def get_help_message(self):
        try:
            message = self.model.objects.get(command_type='help').message
        except self.model.DoesNotExist:
            message = self.default_message
        return message

    def get_about_message(self):
        try:
            message = self.model.objects.get(command_type='about').message
        except self.model.DoesNotExist:
            message = self.default_message
        return message


class Categories:
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
                categories = self.model.objects.filter(parent_category=parent_category)
            except self.model.DoesNotExist:
                return self.model.objects.none()
        else:
            try:
                categories = self.model.objects.filter(parent_category=None)
            except self.model.DoesNotExist:
                return self.model.objects.none()

        return categories
