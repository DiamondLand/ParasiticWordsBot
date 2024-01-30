from gigachat import GigaChat
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from elements.states_group import CheckLiteracy, not_in_state_filter
from elements.inline import back_btn

router = Router()


@router.callback_query(not_in_state_filter, F.data == "check_literacy")
async def start_check_literacy_text(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Для проверки текста (до 1.000 символов) необходимо ввести его в чат:"
    )
    await state.set_state(CheckLiteracy.input)


@router.message(CheckLiteracy.input)
async def check_litracy_text(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(text="Упс! Панель проверки грамотности не была запущена...")
        return

    bot_message = await message.answer("🔎 Думаю...")
    Giga_Chat = GigaChat(
        credentials=message.bot.config["SETTINGS"]["giga_chat_token"], verify_ssl_certs=False
    )
    with Giga_Chat as giga:
        response = giga.chat(
            f'В ответ отправь мне ТОЛЬКО "{message.text[:1000]}" с исправлениями по всем правилам русского языка!'
        )

    await bot_message.edit_text(
        text=f"{response.choices[0].message.content}\n\n<i>Вы можете ввести новый текст до 1.000 символов:</i>",
        reply_markup=back_btn().as_markup()
    )
