import telebot as tg
import webbrowser
token = "7934846315:AAGj3Awh0S_Y8N0tWwnPWaOC4LWjYN2HFIM"

bot = tg.TeleBot(token)

HELP = """
/help - Вывод команд для бота
/start - получить стартовое сообщение
/hot - получить секрет
"""
@bot.message_handler(commands=["site", "web"])
def site(message):
    webbrowser.open("https://ru.pinterest.com/pin/388224430402195688/")

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