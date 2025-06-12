import aiogram 
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import Token

bot = Bot(Token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hi!")

@dp.message(Command("help")) # Позволяет фильтровать команды
async def help(message: Message):
    await message.answer("Это команда /help")

"""
В F - хранится всё что отправляет пользователь в сообщении 
"""

@dp.message(F.text == "How are u?")
async def how_are_you(message: Message):
    await message.answer("Nice! Thank u")

@dp.message(F.photo)
async def photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")

@dp.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIBamhK61xIW-lUXT0Capn0CYdb0FiAAAKg-jEbXiRYSgABh1OCfwSXvAEAAwIAA3gAAzYE", caption="He's Billy Herrington")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")