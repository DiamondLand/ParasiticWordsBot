import configparser
import asyncio

from gigachat import GigaChat
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode

from loguru import logger

config = configparser.ConfigParser()
config.read("configs/config.ini")

bot = Bot(config["SETTINGS"]["token"], parse_mode=ParseMode.HTML)

dp = Dispatcher()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Bot successfully launched!")
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(text="Здравствуйте, Я - Telegram бот на основе GigaChat, всегда просматривающий наш с Вами чат.\n\nНапишите любое слово и я скажу является ли оно словом-паразитом, либо нет 💖!")


@dp.message(F.text)
async def check_messages(message: Message):
    bot_message = await message.answer("🔎 Думаю...")
    Giga_Chat = GigaChat(
        credentials=config["SETTINGS"]["giga_chat_token"], verify_ssl_certs=False
    )
    with Giga_Chat as giga:
        response = giga.chat(
            f'Скажи мне, слово {message.text} является словом-паразитом? Нужен ответ только "является" или "не является"'
        )

    await bot_message.edit_text(text=response.choices[0].message.content)


if __name__ == "__main__":
    asyncio.run(main())
