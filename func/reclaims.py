import telebot
import time
import datetime
from telebot.types import ReplyKeyboardMarkup # Es la libreria para crear botones


import settings.settings as settings

bot = telebot.TeleBot(settings.TOKEN)

def reclaim(message):
    markup = ReplyKeyboardMarkup(
        one_time_keyboard=False,
        input_field_placeholder="Pulsa un boton",
        resize_keyboard=True
    )
    markup.add("Home 🏘")
    bot.send_message(message.chat.id,"👍")
    bot.send_message(message.chat.id,"Gracias por contar con nosotros. Leeremos su queja con gusto\nDentro de unos minutos le atenderemos",reply_markup=markup)
    if message.chat.last_name == None:
        segundo_nombre = ""
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
    markup = ReplyKeyboardMarkup(
        one_time_keyboard=False,
        input_field_placeholder="Pulsa un boton",
        resize_keyboard=True
    )
    markup.add("Home 🏘")
    bot.send_message(message.chat.id,"👍")
    bot.send_message(message.chat.id,"Gracias por contar con nosotros. Leeremos su sugerencia con gusto\nDentro de unos minutos le atenderemos",reply_markup=markup)
    if message.chat.last_name == None:
        segundo_nombre = ""
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
        
def duda(message):
    markup = ReplyKeyboardMarkup(
        one_time_keyboard=False,
        input_field_placeholder="Pulsa un boton",
        resize_keyboard=True
    )
    markup.add("Home 🏘")
    bot.send_message(message.chat.id,"👍")
    bot.send_message(message.chat.id,"Gracias por contar con nosotros. Leeremos su sugerencia con gusto\nDentro de unos minutos le atenderemos",reply_markup=markup)
    if message.chat.last_name == None:
        segundo_nombre = ""
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


def home(message):
    foto = open('./public/logo.jpg','rb')
    markup = ReplyKeyboardMarkup(
        one_time_keyboard=False,
        input_field_placeholder="Pulsa un boton",
        resize_keyboard=True
    )
    markup.add("Queja 🚫","Sugerencia 🆗",)
    markup.add("Dudas ❓","Otro ✉️")
    # bot.send_message(message.chat.id,f"Hola <b>{message.chat.first_name}</b>\n"+settings.HOME_MESSAGE,"html",reply_markup=markup)
    bot.send_photo(message.chat.id,foto,f"Hola <b>{message.chat.first_name}</b>\n"+settings.HOME_MESSAGE,"html",reply_markup=markup)