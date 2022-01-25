# IMPORT DEPENDENCIES 
import dotenv
import telebot
import os 
import dotenv
from supersecrete.computation import supercomplexOnlyLocalFunction

# LOAD TOKEN TO ACCESS THE BOT
dotenv.load_dotenv()
API_key   = os.environ.get('API_KEY')



bot = telebot.TeleBot(API_key, parse_mode=None)
@bot.message_handler(commands=['ping'])
def send_welcome(message):
    pong = supercomplexOnlyLocalFunction()
    bot.reply_to(message, pong)

# @bot.message_handler(commands=['passengers'])
# def send_photo(message):
#     bot.send_chat_action(message.chat.id, 'upload_photo')
#     img = open('graph.png', 'rb')
#     bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
#     img.close()


bot.infinity_polling()


