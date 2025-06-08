import telebot as tg
import sqlite3

token = ""
bot = tg.TeleBot(token)
name = None

@bot.message_handler(commands=["start"])
def start(message):
    # создание базы данных
    conn = sqlite3.connect("baza.sql")
    cur = conn.cursor()   #Курсор 

    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primaty key, name varchar(50), pass varchar(50))") # Позволяет выполнять некоторые sql-команды
    conn.commit() # Синхронизирует все изменения 
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "Hello! Now we're registering you! Please, write you first_name")
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    # strip() -позволяет удалить пробелы до и после
    bot.send_message(message.chat.id, "Write your password")
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    global name
    # регистрируем пользователя
    conn = sqlite3.connect("baza.sql")
    cur = conn.cursor()   #Курсор 

    cur.execute("INSERT INTO users (name, pass) VALUES('%s', '%s')" % (name, password))
    conn.commit() # Синхронизирует все изменения 
    cur.close()
    conn.close()
    
    markup = tg.types.InlineKeyboardMarkup()
    markup.add(tg.types.InlineKeyboardButton("user's list", callback_data="users"))
    bot.send_message(message.chat.id, "You're sign up! Congratulation!", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback(call):
    conn = sqlite3.connect("baza.sql")
    cur = conn.cursor()   #Курсор 

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    info = ""
    for el in users:
        info += f"Name: {el[1]}, Password: {el[2]}\n"

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)



bot.polling(non_stop=True)