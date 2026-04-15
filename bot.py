import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton
)

BOT_TOKEN = "8634842300:AAFlAsZ5MBl8BUwOlYt8INP1DsaSzCDW-sM"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👨‍🏫 Тренеры"), KeyboardButton(text="💰 Цены")],
            [KeyboardButton(text="🗓 Расписание"), KeyboardButton(text="🏆 Турниры")],
            [KeyboardButton(text="🎁 Акции и скидки"), KeyboardButton(text="📚 Новичкам")],
            [KeyboardButton(text="📞 Связаться с нами")],
        ],
        resize_keyboard=True
    )

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "♟ Добро пожаловать в <b>ChessLab</b> — онлайн-школу шахмат!\n\n"
        "Здесь вы найдёте всё о наших занятиях, тренерах, расписании и ценах.\n\n"
        "Выберите раздел 👇",
        parse_mode="HTML",
        reply_markup=main_menu()
    )

@dp.message(F.text == "👨‍🏫 Тренеры")
async def trainers(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💰 Посмотреть цены", callback_data="prices")],
        [InlineKeyboardButton(text="📞 Записаться", url="https://t.me/diana_zakarian")],
    ])
    await message.answer(
        "👩‍🏫 <b>Диана Закарьян — главный тренер</b>\n"
        "Основатель ChessLab, 6+ лет опыта. Ученики регулярно занимают призовые места на турнирах.\n\n"
        "♟ <b>Георгий Орлов — тренер</b>\n"
        "КМС, бронзовый призёр Первенства ЮФО, многократный чемпион Сочи, победитель международных фестивалей.\n\n"
        "🌺 <b>Виктория — тренер</b>\n"
        "10+ лет игры, 1 взрослый разряд. Победительница первенства Пятигорска, призёр первенств Ставропольского края и СКФО. 3+ года преподавания.",
        parse_mode="HTML",
        reply_markup=kb
    )

@dp.message(F.text == "💰 Цены")
async def prices(message: types.Message):
    await show_prices(message)

@dp.callback_query(F.data == "prices")
async def prices_callback(call: types.CallbackQuery):
    await show_prices(call.message)
    await call.answer()

async def show_prices(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📞 Записаться", url="https://t.me/diana_zakarian")],
        [InlineKeyboardButton(text="🎁 Акции и скидки", callback_data="discounts")],
    ])
    await message.answer(
        "💰 <b>Цены на занятия</b>\n\n"
        "🟡 <b>Групповые занятия</b> — 6 000 ₽/мес\n"
        "Тренер: Диана или Георгий\n\n"
        "━━━━━━━━━━━━━━━━━\n"
        "👤 <b>Индивидуальные занятия</b>\n"
        "<i>Георгий / Виктория</i>\n"
        "• 30 мин — 1 000 ₽\n"
        "• 45 мин — 1 500 ₽\n"
        "• 60 мин — 2 000 ₽\n\n"
        "━━━━━━━━━━━━━━━━━\n"
        "👥 <b>Парные занятия</b> <i>(цена с человека)</i>\n"
        "<i>Георгий / Виктория</i>\n"
        "• 30 мин — 750 ₽\n"
        "• 45 мин — 1 000 ₽\n"
        "• 60 мин — 1 250 ₽",
        parse_mode="HTML",
        reply_markup=kb
    )

@dp.message(F.text == "🗓 Расписание")
async def schedule(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 Открыть расписание", url="https://chess-lab.yonote.ru/share/01e6a4eb-a3fe-4c52-98fb-d5bda14e5d4b")],
        [InlineKeyboardButton(text="📞 Записаться", url="https://t.me/diana_zakarian")],
    ])
    await message.answer(
        "🗓 <b>Расписание</b>\n\n"
        "• Месячное расписание регулярных активностей — по кнопке ниже\n"
        "• Актуальные недельные турниры — в последнем закреплённом сообщении канала",
        parse_mode="HTML",
        reply_markup=kb
    )

@dp.message(F.text == "🏆 Турниры")
async def tournaments(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 Расписание турниров", url="https://chess-lab.yonote.ru/share/01e6a4eb-a3fe-4c52-98fb-d5bda14e5d4b")],
    ])
    await message.answer(
        "🏆 <b>Турниры ChessLab</b>\n\n"
        "Каждое воскресенье — бесплатный онлайн-турнир по блицу для детей.\n"
        "Участвовать могут все, не только ученики школы!\n\n"
        "Актуальные ссылки — в последнем закреплённом сообщении.",
        parse_mode="HTML",
        reply_markup=kb
    )

@dp.message(F.text == "🎁 Акции и скидки")
async def discounts(message: types.Message):
    await show_discounts(message)

@dp.callback_query(F.data == "discounts")
async def discounts_callback(call: types.CallbackQuery):
    await show_discounts(call.message)
    await call.answer()

async def show_discounts(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 Все акции и скидки", url="https://chess-lab.yonote.ru/share/cecbaf8b-84c5-403d-b1d3-1720c3d14e57")],
        [InlineKeyboardButton(text="📞 Записаться", url="https://t.me/diana_zakarian")],
    ])
    await message.answer(
        "🎁 <b>Акции и скидки</b>\n\nАктуальные предложения — по кнопке ниже.",
        parse_mode="HTML",
        reply_markup=kb
    )

@dp.message(F.text == "📚 Новичкам")
async def for_beginners(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📖 Открыть статью", url="https://chess-lab.yonote.ru/share/8503fa9d-95eb-44ab-b6f2-e56e1df3e57b")],
        [InlineKeyboardButton(text="📞 Записаться", url="https://t.me/diana_zakarian")],
    ])
    await message.answer(
        "📚 <b>Новичкам</b>\n\nЧто подготовить к первому занятию и как решать технические проблемы — в статье по кнопке ниже.",
        parse_mode="HTML",
        reply_markup=kb
    )

@dp.message(F.text == "📞 Связаться с нами")
async def contacts(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✍️ Написать Диане", url="https://t.me/diana_zakarian")],
    ])
    await message.answer(
        "📞 <b>Связь с нами</b>\n\n"
        "👩‍🏫 Диана, главный тренер — @diana_zakarian\n\n"
        "Готовы ответить на любые вопросы по занятиям, расписанию и записи.",
        parse_mode="HTML",
        reply_markup=kb
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
