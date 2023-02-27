import logging
import time

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import misc
from models import Request, Secrets

secrets = misc.load_secrets()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=secrets.BOT_TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет!\nВ этом боте вы можете написать какую картинку хотите получить и я вам ее отправлю!"
    )


@dp.message_handler()
async def get_request(message: types.Message):
    await message.answer("Спасибо за обращение!\nВ ближайщее время ожидайте ответ!")
    request = Request(text=message.text.strip(), tg_chat_id=message.chat.id, discord_webhook=secrets.DISCORD_WEBHOOK)
    misc.send_request(request=request)
    time.sleep(5)
    await send_photo(request)


async def send_photo(request: Request):
    doc = open("image.png", "rb")
    await bot.send_document(
        document=doc,
        caption=f"Фото по запросу: {request.text}",
        chat_id=request.tg_chat_id,
    )


executor.start_polling(dp, skip_updates=True)
