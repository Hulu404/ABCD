
import telebot as tg

token = "7934846315:AAGj3Awh0S_Y8N0tWwnPWaOC4LWjYN2HFIM"

bot = tg.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)