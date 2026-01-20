from aiogram import Router, F
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.admin.kbs import main_admin_kb, admin_back_kb
from app.config import settings
from app.dao.dao import UserDAO, BookingDAO


router = Router()


@router.callback_query(F.data == "admin_panel", F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_start(call: CallbackQuery):
    """
    Обработчик входа в админ-панель. Доступ разрешен только администраторам.
    """
    await call.answer("Доступ в админ-панель разрещен!")
    await call.message.edit_text("Выберите действие:", reply_markup=main_admin_kb())


@router.callback_query(F.data == "admin_panel", F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_start(call: CallbackQuery):
    await call.answer("Доступ в админ-панель разрещен!")
    await call.message.edit_text("Выберите действие:", reply_markup=main_admin_kb())



@router.callback_query(F.data == "admin_users_stats", F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_users_stats(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обработчик запроса статистики пользователей.
    Получает общее количество пользователей в базе данных и отправляет информацию админу.
    """
    await call.answer("Статистика пользователей")
    users_stats = await UserDAO(session_without_commit).count()
    await call.message.edit_text(f'Всего в базе данных {users_stats} пользователей.', reply_markup=admin_back_kb())


@router.callback_query(F.data == "admin_bookings_stats", F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_bookings_stats(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Обработчик запроса статистики бронирований.
    Получает данные о бронированиях, включая общее количество, завершенные, активные и отмененные.
    """
    await call.answer("Загружаю статистику...")
    bookings_stats = await BookingDAO(session_without_commit).book_count()
    booked_count = bookings_stats.get("booked", 0)  # Количество активных бронирований
    completed_count = bookings_stats.get("completed", 0)   # Количество завершенных бронирований
    canceled_count = bookings_stats.get("canceled", 0)  # Количество отмененных бронирований
    total_count = bookings_stats.get("total", 0)    # Общее количество бронирований

    message = (
        "<b>📊 Статистика бронирований:</b>\n\n"
        f"<i>Всего бронирований:</i> <b>{total_count}</b>\n"
        f"✅ <i>Забронировано:</i> <b>{booked_count}</b>\n"
        f"☑️ <i>Завершено:</i> <b>{completed_count}</b>\n"
        f"🚫 <i>Отменено:</i> <b>{canceled_count}</b>"
    )

    await call.message.edit_text(message, reply_markup=admin_back_kb())