from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import StateFilter


# --- StatesGroup для проверки на слова-паразиты ---
class ParasiticWords(StatesGroup):
    input = State()


# --- StatesGroup для проверки на грамотность ---
class CheckLiteracy(StatesGroup):
    input = State()


# --- Блокирующий фильтр для команд во время стадий ---
not_in_state_filter = ~StateFilter(
    ParasiticWords.input,
    CheckLiteracy.input
)
