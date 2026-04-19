import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN
from keyboards import main_keyboard
from schedule_data import SCHEDULE_TEXT, ABOUT_TEXT, HELP_TEXT, MOTIVATION_LIST

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    user_name = message.from_user.first_name if message.from_user else "студент"

    text = (
        f"Привет, <b>{user_name}</b>! 👋\n\n"
        "Я бот онлайн-школы.\n"
        "Помогу тебе быстро посмотреть расписание уроков.\n\n"
        "Выбери нужную кнопку ниже 👇"
    )

    await message.answer(text, reply_markup=main_keyboard)


@router.message(F.text == "📅 Расписание")
async def schedule_handler(message: Message):
    await message.answer(SCHEDULE_TEXT)


@router.message(F.text == "ℹ️ О боте")
async def about_handler(message: Message):
    await message.answer(ABOUT_TEXT)


@router.message(F.text == "🆘 Помощь")
async def help_handler(message: Message):
    await message.answer(HELP_TEXT)


@router.message(F.text == "✨ Мотивация")
async def motivation_handler(message: Message):
    phrase = random.choice(MOTIVATION_LIST)
    await message.answer(f"✨ <b>Мотивация на сегодня:</b>\n\n{phrase}")


@router.message()
async def fallback_handler(message: Message):
    await message.answer(
        "Я пока понимаю только кнопки меню 😊\n"
        "Пожалуйста, выбери нужный раздел ниже.",
        reply_markup=main_keyboard
    )


async def main():
    logging.basicConfig(level=logging.INFO)

    if TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        raise ValueError("Вставь токен в config.py")

    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
