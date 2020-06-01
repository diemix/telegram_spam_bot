#Создатель не несет отственности за ущерб или неудобства которые мог причинить бот.
#The creator is not liable for damage or inconvenience that the bot could cause.

#Use this for fun. Not for revenge.
import time
import telebot
from telebot import types
import random
import string

def get_id(id):
    id = int(id)
    message_number = 0
    while True:
        for counter in range(21):
            send_message(id,message_number)
            message_number+=1
        time.sleep(15)

def check_token(token):
    try:
        bot = telebot.TeleBot(token)
    except:
        token =input("Invalid token.. ")
        check_token(token)
    return bot

def send_message(id, message_number):
    try:
        time.sleep(0.3)
        text = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation + "/start" + "/help") for i in range(1000)])
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        button = types.KeyboardButton(text=text)
        keyboard.add(button, button, button, button, button, button, button, button, button, button, button, button,
                     button, button, button)
        bot.send_message(id, text, reply_markup=keyboard)
        print("Message number",message_number," sent to ", str(id), "        date & time: ", time.asctime())
    except:
        print("Failed to spam ", str(id), "Retrying in 20 secs..        date & time: ", time.asctime())
        time.sleep(20)

def spam(id):
    try:
        id = message.text
        id = int(id)
        message_number = 0
        print("Received id ", message.chat.id, "        date & time: ", time.asctime())
        while True:
            for counter in range(21):
                send_message(id,message_number)
                message_number+=1
            time.sleep(15)
    except:
        sleep(30)
        spam(id)

@bot.message_handlers(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Telegram Bot. Id of this chat - " + message.chat.id)

token = input("Insert token.. ")
bot = check_token(token)
id = input("Insert chat id..")
bot.polling()
