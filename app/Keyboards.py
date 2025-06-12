from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
#Кнопки на месте клавиатуры


main = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="Button1")],
    [KeyboardButton(text="Button2"), KeyboardButton(text="Button2.2")
]],
                        resize_keyboard=True,
                        input_field_placeholder="Выберите пункт меню!"
)


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Baza", url="https://vkvideo.ru/video605599968_456239490?t=1m14s")]])

async def Reply_cars():
    Keyboard = ReplyKeyboardBuilder()
    for car in ["Mers", "Porche", "Aston Martin"]:
        Keyboard.add(KeyboardButton(text=car))
    return Keyboard.adjust(2).as_markup()

async def inline():
    Keyboard = InlineKeyboardBuilder()
    for i, j in zip(["Москва", "Петербург", "Киев"], ["https://t.me/i_am_ludoman404/199", "https://t.me/i_am_ludoman404/185", "https://t.me/i_am_ludoman404/183"]):
        Keyboard.add(InlineKeyboardButton(text=i, url=j))
    return Keyboard.adjust(2).as_markup()
