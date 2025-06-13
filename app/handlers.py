from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.Keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from app.middlewares import TestMiddleware

router = Router()

router.message.outer_middleware(TestMiddleware())

class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Hi, {message.from_user.first_name}!", reply_markup=kb.main)

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


@router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer("You Press catalog")
    await callback.message.edit_text("You Press catalog!", reply_markup=await kb.inline())

@router.callback_query(F.data == "basket")
async def basket(callback: CallbackQuery):
    await callback.answer("You're Winner!")
    await callback.message.edit_text("You press basket", reply_markup=kb.blue)

@router.callback_query(F.data == "return")
async def return_(callback: CallbackQuery):
    await callback.answer("Main")
    await callback.message.edit_text("You on start", reply_markup=kb.main)


@router.message(Command("reg"))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("What's your name?")

@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer("Write your phone number:")

@router.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f"Thank u! You're registered. \nName: {data["name"]}\nNumber: {data["number"]}")
    await state.clear()


