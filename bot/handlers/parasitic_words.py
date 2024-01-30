from gigachat import GigaChat
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from elements.states_group import ParasiticWords, not_in_state_filter
from elements.inline import back_btn

router = Router()


@router.callback_query(not_in_state_filter, F.data == "parasitic_words")
async def start_parasitic_words(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Для проверки на слова-паразиты необходимо ввести их в чат:"
    )
    await state.set_state(ParasiticWords.input)


@router.message(ParasiticWords.input)
async def check_parasitic_words(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(text="Упс! Панель поиска слов-паразитов не была запущена...")
        return

    bot_message = await message.answer("💫 Анализирую...")
    Giga_Chat = GigaChat(
        credentials=message.bot.config["SETTINGS"]["giga_chat_token"], verify_ssl_certs=False
    )
    with Giga_Chat as giga:
        response = giga.chat(
            f'Скажи мне, слово {message.text} является словом-паразитом? Нужен ответ только "является" или "не является"'
        )

    await bot_message.edit_text(
        text=f"{response.choices[0].message.content}\n\n<i>Вы можете ввести новые слова в чат:</i>",
        reply_markup=back_btn().as_markup()
    )
