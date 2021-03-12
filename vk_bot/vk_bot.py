import asyncio

from vkbottle.bot import Message
import vkbottle.bot

from core.settings import VK_TOKEN

if not VK_TOKEN:
    raise ValueError('TG_TOKEN не может быть пустым')


class VkBot(vkbottle.bot.Bot):
    def run_forever(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print('Vk бот запущен...')
        super(VkBot, self).run_forever()


bot = VkBot(VK_TOKEN)


@bot.on.message(text='Начать')
async def start_message_handler(ans: Message):
    """Команда Начать"""
    await ans.answer('Привет!')
