import telebot as tg
from currency_converter import CurrencyConverter
from telebot import types

token = ""
bot = tg.TeleBot(token)
currency =CurrencyConverter()
amount = 0

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, введите сумму:")
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, "Неверный формат. Введите сумму")
        bot.register_next_step_handler(message, summa)
        return
    
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("USD -> EUR", callback_data="usd_eur")
        btn2 = types.InlineKeyboardButton("EUR -> USD", callback_data="eur_usd")
        btn3 = types.InlineKeyboardButton("USD -> RUB", callback_data="usd_rub")
        btn4 = types.InlineKeyboardButton("Другое значение", callback_data="else")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, "Выберите пару валют", reply_markup=markup)
    
    else:
        bot.send_message(message.chat.id, "Сумма должна быть больше 0. Впишите сумму")
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != "else":
        values = call.data.upper().split("_")
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f"Получается: {round(res, 2)}.\n Можете заново ввести сумму:")
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, mycurrency)

def mycurrence(message):

    try:
        values = message.text.upper().split("_")
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f"Получается: {round(res, 2)}.\n Можете заново ввести сумму:")
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, "Что-то не так. Впишите значение заново")
        bot.register_next_step_handler(message, mycurrence)

bot.polling(non_stop=True)
