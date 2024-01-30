from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hlink

from keyboards.inline import main_menu_buttons, back_to_main_menu_button


router = Router()

# --- Основная панель ---
@router.message(Command("start", "shedule"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать, <b>дорогой студент</b>, чем тебе помочь 💖?",
        reply_markup=main_menu_buttons().as_markup()
    )


# --- Обработчик кнопки возвращения в основное меню ---
@router.callback_query(F.data == "back_to_main_menu")
async def back_to_main_menu_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Добро пожаловать, <b>дорогой студент</b>, чем тебе помочь 💖?",
        reply_markup=main_menu_buttons().as_markup()
    )


# --- Обработчик кнопки запроса в поддержку ---
@router.callback_query(F.data == "connect_with_support")
async def connect_with_support_btn(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f"Для связи с поддержкой необходимо подключиться к <b>{hlink('нашему каналу', 'https://t.me/+Z9Igbpt-16MwZWYy')}</b> и задать вопрос под закреплённым постом.",
        reply_markup=back_to_main_menu_button().as_markup()
    )
