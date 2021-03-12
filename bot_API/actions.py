from bot_API.models import BotInfo
from core.settings import BOT_PLATFORMS


class ChatBotActions:
    model = BotInfo
    platform = ''
    object = None

    def check_platform(self):
        for platform in BOT_PLATFORMS:
            if self.platform == platform[0]:
                break
        else:
            raise ValueError(f'Указана не существующая платорма. '
                             f'Доступные: '
                             f'{[platform[0] for platform in BOT_PLATFORMS]}')

    def get_object(self):
        return self.model.objects.get(platform=self.platform)

    def get_start_message(self):
        start_message = self.get_object().start_message
        start_message = start_message if start_message else 'Привет!'
        return start_message

    def get_help_message(self):
        pass

    def get_about_message(self):
        pass
