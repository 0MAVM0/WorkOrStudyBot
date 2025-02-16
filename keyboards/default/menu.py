from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="👨‍🦰 Colleague"),
            KeyboardButton(text="💼 Work  Place 🏢"),
        ],
        [
            KeyboardButton(text="👨‍💼 Worker"),
            KeyboardButton(text="👩‍🏫 Teacher"),
        ],
        [
            KeyboardButton(text="👨‍🎓 Student")
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True
)
