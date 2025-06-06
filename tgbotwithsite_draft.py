import telebot as tg
import webbrowser
from telebot import types
token = ""

bot = tg.TeleBot(token)

HELP = """
/help - Вывод команд для бота
/start - получить стартовое сообщение
/hot - получить секрет
"""

def on_click(message):
    if message.text == "Ссылка на сайт":
        bot.send_message(message.chat.id, "Website is open")
    elif message.text == "Удалить фото":
        bot.send_message(message.chat.id, "Фото удаленно")

# Отправка файла 
# Кнопки внутренние (которые появляются на месте клавиатуры)
@bot.message_handler(commands=["main"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton("Ссылка на сайт")
    markup.row(bt1)
    bt2 = types.KeyboardButton("Удалить фото")
    bt3 = types.KeyboardButton("Изменить текст")
    markup.row(bt2, bt3)
    file = open("D:\Telegram\photo_2025-06-04_15-24-11.jpg", "rb")
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, "GGHF!", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


# Кнопки внешние(которые отправляет бот с сообщением)

@bot.message_handler(content_types=["photo", "video", "audio"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton("Ссылка на сайт", url="https://google.com")
    markup.row(bt1)
    bt2 = types.InlineKeyboardButton("Удалить фото", callback_data="delete")
    bt3 = types.InlineKeyboardButton("Изменить текст", callback_data="edit")
    markup.row(bt2, bt3)
    bot.reply_to(message, "Классное фото!", reply_markup=markup)

# Алгоритм выполнения при нажатии той, или иной кнопки

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data ==  "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1) # Удаление предпоследнего сообщения
    elif callback.data ==  "edit":
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)
@bot.message_handler(commands=["site", "web"])
def site(message):
    webbrowser.open("https://google.com")

@bot.message_handler(commands=["start", "Привет!"])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}!")


@bot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}!")
    elif message.text.lower() == "id":
        bot.reply_to(message, f"ID: {message.from_user.id}")     

bot.polling(non_stop=True)