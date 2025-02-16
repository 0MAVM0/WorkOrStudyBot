from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from data.config import ADMINS
from keyboards.default.menu import menu

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = f"Hello, *{message.from_user.full_name}*👋!\n"
    text += "Welcome to our *bot*🤖, which hels to find a _work_💼 "
    text += "or course to _study_👩‍🎓."
    # for admin in ADMINS:
    #     await bot.send_message(chat_id=admin, text=text)
    await message.answer(text=text, parse_mode="Markdown", reply_markup=menu)
