import telebot as tg
import random
token = ""

bot = tg.TeleBot(token)

HELP = '''
/help - Вывести список команд
/add - Добавить дела в список
/random - Случайное дело
/print - Вывести список
'''
tasks = {}


def add_To_DO(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add_to(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_To_DO(date, task)
    text = f"Задача {task} добавлена на дату {date}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "cегодня"
    RANDOM_TASKS = [
        "Собрать ракету",
        "Мумию встретить",
        "На Эйфелеву башню влезть"]
    task = random.choice(RANDOM_TASKS)
    add_To_DO(date, task)
    text = f"Задача {task} добавлена на дату {date}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['print'])
def show_(message):
    k = message.text.split(maxsplit=1)
    date = k[1].lower()
    if date in tasks:
        text = date.upper()
        for task in tasks[date]:
            text += f"[] {tasks}\n"
    else:
        text = f"Такой даты нет"
    bot.send_message(message.chat.id, text)



bot.polling(none_stop=True)