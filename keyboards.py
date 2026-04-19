from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Расписание")],
        [KeyboardButton(text="ℹ️ О боте"), KeyboardButton(text="🆘 Помощь")],
        [KeyboardButton(text="✨ Мотивация")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери нужный раздел..."
)
