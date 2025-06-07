import requests 
import telebot as tg
from bs4 import BeautifulSoup
import types

token = ""
bot = tg.TeleBot(token)
url = "https://yandex.ru/pogoda/ru/213?lat=55.723705&lon=37.562866&utm_campaign=informer&utm_content=main_informer&utm_medium=web&utm_source=home"

@bot.message_handler(commands=["start", "Привет!"])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}!")

@bot.message_handler(commands=["temp"])
def get_temp(message):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    temp = bs.find("span", class_="AppFactTemperature_value__2qhsG").get_text()
    text = f"В москве сейчас: {temp}"
    bot.send_message(message.chat.id, text)
    
@bot.message_handler(commands=["hot"])
def hot_command(message):
    hot(message)

def hot(message):
    with open("", "rb") as video_file:
        bot.send_video(message.chat.id, video_file, caption="Вот видео", supports_streaming=True)
            

    
    

bot.polling(non_stop=True)



