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
#bot_id = 706930638
global kol_soob
global id_new_member
global Otvet_new_membera
Otvet_new_membera = False
id_new_member = -1
kol_soob = -1
@bot.message_handler(content_types=['new_chat_members'])
def welcome_chat(message : Message):
    global id_new_member
    global chat_id
    global name_new_member
    global flag_new_chat_member
    global kol_soob
    global Soglas_user
    global Otvet_new_membera
    Otvet_new_membera = False
    Soglas_user = False
    kol_soob = 0
    flag_new_chat_member=True
    chat_id = message.chat.id
    name_new_member = message.new_chat_member.first_name
    id_new_member = message.new_chat_member.id
    if(id_new_member == 706930638):
            pass
    else:
        bot.send_message(chat_id,'{0}, добро пожаловать в клуб предпринимателей Life&Business'.format(name_new_member))
        time.sleep(1)
        bot.send_message(chat_id,'{0}, хочешь рассказать о себе?\n(да/нет)'.format(name_new_member))
        kol_soob+=1
        #bot.register_next_step_handler(msg, Vopros_1)
@bot.message_handler(content_types = ['text'])
def raz(Message):
    global kol_soob
    global Soglas_user
    global id_new_member, Otvet_new_membera
    user_id = Message.from_user.id
    if(user_id == id_new_member and Otvet_new_membera == False):
        text_mess = Message.text.lower()
        if(text_mess == 'да'):
            Soglas_user = True
            Otvet_new_membera = True
        elif(text_mess == 'нет'):
            Soglas_user = False
            Otvet_new_membera = True
            kol_soob = -1
            FAQ = 'Полезная информация о клубе находится в закрепленном сообщении'
            zacl = 'Если остались вопросы, задавай '
            bot.send_message(chat_id,'{0}\n{1}'.format(FAQ,zacl))
    #print(kol_soob)
    if (kol_soob == 1):
        Vopros_1(Message)
    elif(kol_soob == 2):
        Vopros_2(Message)
    elif(kol_soob == 3):
        Vopros_3(Message)
    elif(kol_soob == 4):
        Tsel_and_Mechta(Message)
    elif(kol_soob == 5):
        Zacl(Message)
def Vopros_1(message : Message):
    if(flag_new_chat_member == True):
        user_id = message.from_user.id
        global kol_soob
        global Soglas_user
        global name_new_member
        if(user_id == id_new_member and kol_soob == 1 and Soglas_user == True):
            time.sleep(3)
            kol_soob+=1
            msg = bot.send_message(chat_id, '{0}, ответь на 3 вопроса:\n1.Каковы твои достижения?'.format(name_new_member))
            bot.register_next_step_handler(msg, Vopros_2)
def Vopros_2(message : Message):
    if(flag_new_chat_member == True):
        user_id = message.from_user.id
        global kol_soob
        global Soglas_user
        if(user_id == id_new_member and kol_soob == 2 and Soglas_user == True):
            time.sleep(3)
            kol_soob+=1
            msg = bot.send_message(chat_id, '2.Чем ты можешь быть полезен для других?')
            bot.register_next_step_handler(msg, Vopros_3)
#@bot.message_handler(content_types = ['text'])
def Vopros_3(message : Message):
    user_id = message.from_user.id
    global kol_soob
    global Soglas_user
    if (user_id == id_new_member and kol_soob == 3 and Soglas_user == True):
        time.sleep(3)
        kol_soob+=1
        msg = bot.send_message(chat_id, '3.В чём тебе нужна помощь?')
        bot.register_next_step_handler(msg, Tsel_and_Mechta)
#@bot.message_handler(content_types = ['text'])
def Tsel_and_Mechta(message : Message):
    user_id = message.from_user.id
    global kol_soob
    global Soglas_user
    if (user_id == id_new_member and kol_soob == 4 and Soglas_user == True):
        time.sleep(3)
        kol_soob+=1
        msg = bot.send_message(chat_id, 'Можешь описать свои цели и мечту')
        bot.register_next_step_handler(msg, Zacl)
#@bot.message_handler(content_types = ['text'])
def Zacl(message : Message):
    global flag_new_chat_member
    global kol_soob
    global Soglas_user
    user_id = message.from_user.id
    if (user_id == id_new_member and kol_soob == 5 and Soglas_user == True):
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
