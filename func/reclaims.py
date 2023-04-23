import telebot
import time
import datetime
from telebot.types import ReplyKeyboardMarkup # Es la libreria para crear botones


import settings.settings as settings

bot = telebot.TeleBot(settings.TOKEN)

def reclaim(message):
    bot.send_message(message.chat.id,"👍")
    bot.send_message(message.chat.id,"Gracias por contar con nosotros. Leeremos su ... con gusto")
    if message.chat.last_name == None:
        segundo_nombre = ""
        print(message)
    else:
        segundo_nombre = message.chat.last_name
    for admin in settings.admins:
        bot.send_message(admin,f"""
<b>Usuario:</b> @{message.chat.username}
<b>Nombre:</b> {message.chat.first_name} {segundo_nombre}
<b>Tipo:</b> Queja 🚫
<b>Contenido</b>
{message.text}
                        """,parse_mode="html")
        
def sugerencia(message):
    bot.send_message(message.chat.id,"👍")
    bot.send_message(message.chat.id,"Gracias por contar con nosotros. Leeremos su sugerencia con gusto")
    if message.chat.last_name == None:
        segundo_nombre = ""
        print(message)
    else:
        segundo_nombre = message.chat.last_name
    for admin in settings.admins:
        bot.send_message(admin,f"""
<b>Usuario:</b> @{message.chat.username}
<b>Nombre:</b> {message.chat.first_name} {segundo_nombre}
<b>Tipo:</b> sugerencia 🆗
<b>Contenido</b>
{message.text}
                        """,parse_mode="html")

def private_reclaims(message):
    msg = bot.send_message(message.chat.id,"Muy bien, a continuacion escriba su queja")
    return msg

def private_sujest(message):
    msg = bot.send_message(message.chat.id,"Muy bien, a continuacion escriba su sugerencia")
    return msg
