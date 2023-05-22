import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineKeyboardMarkup

import func.reclaims as reclaims
import settings.settings as settings

from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply

bot = telebot.TeleBot(settings.TOKEN)

@bot.message_handler(commands=["start"])
def start_function(message):
    reclaims.home(message)

@bot.message_handler(commands=["try"])
def try_command(message):
    bot.send_chat_action(message.chat.id,"typing")
    bot.send_message(message.chat.id,f"Gracias por escribirme {message.chat.first_name}")
    bot.send_message(841744845,f"Usuario: {message.chat.username}\nID es: {message.chat.id}")
    
@bot.message_handler(commands=["contact"])
def reclamacion_function(message):
    reclaims.private_reclaims(message)
    
@bot.message_handler(commands=['links'])
def links(message):
    bot.send_message(message.chat.id,'''
Esta es la Lista de nuestros Sitios
<b><a href="www.ipvcecubavirtual.wordpress.com">Pagina Web</a> 🌐
<a href="https://t.me/ipvcecubagrupo">Grupo de Telegram</a> 👥
<a href="https://t.me/virtualipvcecuba">Canal de Telegram</a> 📺
<a href="https://instagram.com/_ipvce?igshid=YmMyMTA2M2Y=">Instagram</a> 📷
<a href="https://www.facebook.com/ipvcecuba?mibextid=ZbWKwL">facebook</a> 📘
</b>                   
                    ''',parse_mode="html")
    
@bot.message_handler(content_types=['text'])
def mensaje(message):
    if message.text == "Queja 🚫":
        msg = reclaims.private_reclaims(message)
        bot.register_next_step_handler(msg,reclaims.reclaim)
    elif message.text == "Sugerencia 🆗":
        msg = reclaims.private_sujest(message)
        bot.register_next_step_handler(msg,reclaims.sugerencia)
    elif message.text == "Dudas ❓":
        msg = reclaims.private_sujest(message)
        bot.register_next_step_handler(msg,reclaims.sugerencia)
    elif message.text == "Home 🏘":
        reclaims.home(message)
    else:
        bot.send_message(message.chat.id,"Lo siento, no entiendo a que te refieres")
    

    
if __name__ == "__main__":
    mensaje = bot.send_message(841744845,"Hola?")
    bot.set_my_commands([
        telebot.types.BotCommand("/start","Inicia El Bot"),
        telebot.types.BotCommand("/ayuda","Mensaje de Ayuda"),
        telebot.types.BotCommand("/links","Muestra los enlaces a nuestros sitios"),
        telebot.types.BotCommand("/contact","Contactanos")
    ])
    print("Todos los sistemas operativos")
    bot.infinity_polling()