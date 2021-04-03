from bot_API import models


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
