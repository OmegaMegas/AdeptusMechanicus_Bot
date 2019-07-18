#110948
import data1
import time
#import random
#import requests
import telebot
from telebot import apihelper
from telebot.types import Message
apihelper.proxy = {"https": "socks5://127.0.0.1:9150"}
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
    global kol_soob
    kol_soob = 0
    flag_new_chat_member=True
    chat_id = message.chat.id
    name_new_member = message.new_chat_member.first_name
    id_new_member = message.new_chat_member.id
    bot.send_message(chat_id,'{0}, добро пожаловать в клуб предпринимателей Life&Business'.format(name_new_member))
    time.sleep(1)
    msg = bot.send_message(chat_id, '{0}, расскажи о себе и ответь на 3 вопроса:\n1.Каковы твои достижения?'.format(name_new_member))
    kol_soob+=1
    bot.register_next_step_handler(msg, Vopros_2)
@bot.message_handler(content_types = ['text'])
def raz(Message):
    global kol_soob
    if (kol_soob == 1):
        Vopros_2(Message)
    elif(kol_soob == 2):
        Vopros_3(Message)
    elif(kol_soob == 3):
        Tsel_and_Mechta(Message)
    elif(kol_soob == 4):
        Zacl(Message)
def Vopros_2(message : Message):
    if(flag_new_chat_member == True):
        user_id = message.from_user.id
        global kol_soob
        if(user_id == id_new_member and kol_soob == 1):
            time.sleep(3)
            kol_soob+=1
            msg = bot.send_message(chat_id, '2.Чем ты можешь быть полезен для других?')
            bot.register_next_step_handler(msg, Vopros_3)
#@bot.message_handler(content_types = ['text'])
def Vopros_3(message : Message):
    user_id = message.from_user.id
    global kol_soob
    if (user_id == id_new_member and kol_soob == 2):
        time.sleep(3)
        kol_soob+=1
        msg = bot.send_message(chat_id, '3.В чём тебе нужна помощь?')
        bot.register_next_step_handler(msg, Tsel_and_Mechta)
#@bot.message_handler(content_types = ['text'])
def Tsel_and_Mechta(message : Message):
    user_id = message.from_user.id
    global kol_soob
    if (user_id == id_new_member and kol_soob == 3):
        time.sleep(3)
        kol_soob+=1
        msg = bot.send_message(chat_id, 'Можешь описать свои цели и мечту')
        bot.register_next_step_handler(msg, Zacl)
#@bot.message_handler(content_types = ['text'])
def Zacl(message : Message):
    global flag_new_chat_member
    global kol_soob
    user_id = message.from_user.id
    if (user_id == id_new_member and kol_soob == 4):
        time.sleep(3)
        motiv = {'Мы рады, что ты присоединился к нам именно сейчас!\n'
                'Возьми ответственность за свою жизнь на себя\n'
                'Ты на пути больших перемен\n'
                'Мы верим в тебя. Мечтай и начни действовать!'}
        FAQ = {'Полезная информация о клубе находится в закрепленном сообщении'}
        zacl = {'Если остались вопросы, задавай '}
        bot.send_message(chat_id, motiv)
        time.sleep(3)
        bot.send_message(chat_id, FAQ)
        time.sleep(3)
        kol_soob+=1
        msg = bot.send_message(chat_id, zacl)
        bot.clear_step_handler(msg)
        #name_new_member = None
bot.polling(none_stop=True)
