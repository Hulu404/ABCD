from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import app.Keyboards as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Hi, {message.from_user.first_name}!", reply_markup=await kb.inline())

@router.message(Command("help")) # Позволяет фильтровать команды
async def help(message: Message):
    await message.answer("Это команда /help")

"""
В F - хранится всё что отправляет пользователь в сообщении 
"""

@router.message(F.text == "How are u?")
async def how_are_you(message: Message):
    await message.answer("Nice! Thank u")

@router.message(F.photo)
async def photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")


@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIBamhK61xIW-lUXT0Capn0CYdb0FiAAAKg-jEbXiRYSgABh1OCfwSXvAEAAwIAA3gAAzYE", caption="He's Billy Herrington")
