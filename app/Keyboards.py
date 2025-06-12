from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
#Кнопки на месте клавиатуры

site = "https://hd.kinopoisk.ru/film/41a971dd517a30f9b86d20def219c326?content_tab=series&episode=9&playingContentId=47d719b99436e165b67898e6b71af7a2&season=2&watch="

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data="catalog")],
    [InlineKeyboardButton(text="Корзина", callback_data="basket"),
    InlineKeyboardButton(text="Контакты", callback_data="contacts")]
])

blue = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Good music", url=site)],
    [InlineKeyboardButton(text="Motivation", url="https://vkvideo.ru/video605599968_456239490?t=1m31s")],
    [InlineKeyboardButton(text="Назад", callback_data="return")]
]) 


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Baza", url=site)]])

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
