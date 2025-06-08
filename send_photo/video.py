import telebot
from telebot import types


token = ""
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton("Сайт Хабра", url="https://habr.com/ru/sandbox/163347/")
    bt2 = types.InlineKeyboardButton("База", url="https://vkvideo.ru/video605599968_456239490")
    markup.add(bt1, bt2)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!", reply_markup=markup)

# @bot.message_handle(commands=["baza"])
# def baza(message):
#     pass
    
bot.polling(non_stop=True)