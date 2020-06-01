import time
import telebot
from telebot import types
import random
import string
import configparser
import os
from messages import *

def create_config(token, file):
    config = configparser.ConfigParser()
    config.add_section("info")
    config.set("info", "token", token)

    with open(file, "w") as config_file:
        config.write(config_file)

def set_up_bot():
    if not os.path.exists("token.ini"):
        token = input('Insert bot token..')
        create_config(token, "token.ini")
    else:
        config = configparser.ConfigParser()
        config.read("token.ini")
        token = config.get("info", "token")
    return token

def spam():
    id = input("Insert chat id.. ")
    print("Spamming..")
    message_number = 0
    while True:
        for counter in range(18):
            message_number += 1
            send_message(id, message_number)
        time.sleep(10)
        spam()

def send_message(id, message_number):
    time.sleep(0.3)
    text = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(1000)])
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    button = types.KeyboardButton(text=text)
    keyboard.add(button, button, button, button, button, button, button, button, button, button, button)
    bot.send_message(id, text, reply_markup=keyboard)
    print("Message number", message_number, " sent to ", str(id), "        date & time: ", time.asctime())

bot = telebot.TeleBot(set_up_bot())
spam()
bot.polling()
