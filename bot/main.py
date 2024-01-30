import configparser
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from loguru import logger
from elements.inline import what_do_choice_btn

from handlers import check_litracy
from handlers import parasitic_words

config = configparser.ConfigParser()
config.read("bot/configs/config.ini")

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.clear()

    await message.answer(
        text="<b>Привет 💝!</b>\nЧем могу тебе помочь?",
        reply_markup=what_do_choice_btn().as_markup()
    )


@dp.callback_query(F.data == "to_main_menu")
async def cmd_back_to_start(callback_query: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.clear()

    await callback_query.message.edit_text(
        text="<b>Привет 💝!</b>\nЧем могу тебе помочь?",
        reply_markup=what_do_choice_btn().as_markup()
    )


async def main():
    bot = Bot(config["SETTINGS"]["token"], parse_mode=ParseMode.HTML)
    bot.config = config

    # --- Подключение модулей ---
    logger.info("Loading modules...")
    dp.include_routers(
        check_litracy.router,
        parasitic_words.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    logger.success("Bot successfully launched")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
