from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# --- Кнопки выбора действия ---
def what_do_choice_btn() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Проверить слова-паразиты",
            callback_data="parasitic_words"
        ),
        InlineKeyboardButton(
            text="Проверить грамотность",
            callback_data="check_literacy"
        )
    )
    return builder


def back_btn() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Назад ↩",
            callback_data="to_main_menu"
        )
    )
    return builder