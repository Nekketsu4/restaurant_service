from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_admin_kb() -> InlineKeyboardMarkup:
    """
    Функция создаёт клавиатуру для главного меню админ-панели.
    """
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="📊 Статистика по пользователям", callback_data="admin_users_stats"))
    kb.add(InlineKeyboardButton(text="📈 Статистика по броням", callback_data="admin_bookings_stats"))
    kb.add(InlineKeyboardButton(text="🏠 На главную", callback_data="back_home"))
    kb.adjust(1)    # Распологаем кнопки в один столбец
    return kb.as_markup()

def admin_back_kb() -> InlineKeyboardMarkup:
    """
    Функция создаёт клавиатуру для возврата в админ-панель.
    """
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_panel"))
    kb.add(InlineKeyboardButton(text="🏠 На главную", callback_data="back_home"))
    kb.adjust(1)
    return kb.as_markup()