#110948
import data1
import time
#import random
#import requests
import telebot
#from telebot import apihelper
from telebot.types import Message
#apihelper.proxy = {"https": "socks5://127.0.0.1:9150"}
token=data1.data_token()
#print(token)
bot = telebot.TeleBot(token)
########################################################
#admin = 123
@bot.message_handler(content_types=['new_chat_members'])
def welcome_chat(message : Message):
    global id_new_member
    global chat_id
    global name_new_member
    global flag_new_chat_member
    flag_new_chat_member=True
    chat_id = message.chat.id
    name_new_member = message.new_chat_member.first_name
    id_new_member = message.new_chat_member.id
    msg = bot.send_message(chat_id,'Здравствуй {0}'.format(name_new_member))
    bot.register_next_step_handler(msg, asks_and_3_quest)
@bot.message_handler(content_types = ['text'])
def asks_and_3_quest(message : Message):
    if(flag_new_chat_member == True):
        user_id = message.from_user.id
        if(user_id == id_new_member):
            time.sleep(3)
            msg = bot.send_message(chat_id, '{0}, расскажи о себе'.format(name_new_member))
            bot.register_next_step_handler(msg, FAQ_TSEL)
@bot.message_handler(content_types = ['text'])
def FAQ_TSEL(message : Message):
    user_id = message.from_user.id
    if (user_id == id_new_member):
        bot.send_message(chat_id, 'Мы - клуб L&B ...FAQ')
        time.sleep(4)
        msg = bot.send_message(chat_id, '{0}, опиши свою цель'.format(name_new_member))
        bot.register_next_step_handler(msg, Dostich_TSEL)
@bot.message_handler(content_types = ['text'])
def Dostich_TSEL(message : Message):
    user_id = message.from_user.id
    if (user_id == id_new_member):
        time.sleep(3)
        msg = bot.send_message(chat_id, 'Каким наилучшим способом ты можешь достичь цели?')
        bot.register_next_step_handler(msg, Vajnost)
@bot.message_handler(content_types = ['text'])
def Vajnost(message : Message):
    user_id = message.from_user.id
    if (user_id == id_new_member):
        time.sleep(3)
        msg = bot.send_message(chat_id, 'Почему это для тебя важно?')
        bot.register_next_step_handler(msg, Zacl)
@bot.message_handler(content_types = ['text'])
def Zacl(message : Message):
    global flag_new_chat_member
    user_id = message.from_user.id
    if (user_id == id_new_member):
        time.sleep(3)
        zacl = {'Мы рады, что ты присоединился к нам именно сейчас!\n'
                'Возьми ответственность за свою жизнь на себя\n'
                'Ты на пути больших перемен\n'
                'Мы верим в тебя. Мечтай и начни действовать!'}
        msg = bot.send_message(chat_id, zacl)
        bot.clear_step_handler(msg)
        #name_new_member = None
    flag_new_chat_member = False
bot.polling(none_stop=True)