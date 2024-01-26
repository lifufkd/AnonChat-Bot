#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import telebot

from Frontend import Bot_buttons, Bot_phrase

############static variables#####################
TG_api = '6756599068:AAEAxP8t_6eJA6YZ_a86Y89DHfOjnC09ark'
DB_path = 'db.sqlite3'
admins = [818895144, 1897256227]
#################################################

bot = telebot.TeleBot(TG_api)

@bot.message_handler(commands=['start', 'admin'])
def comand(message):
    command = message.text.replace('/', '')
    user_ID = message.from_user.id
    phrases = Bot_phrase()
    buttons = Bot_buttons()
    if command == 'start':
        bot.reply_to(message, phrases.get_phrase_pac('RU', 'global')[0])
        bot.send_message(message.chat.id, phrases.get_phrase_pac('RU', 'global')[1], reply_markup=buttons.start_buttons())
    elif command == 'admin':
        pass


@bot.message_handler(content_types=['photo', 'video', 'voice', 'audio', 'image', 'sticker', 'text'])
def content(message):
    pass

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_ID = call.message.chat.id

bot.polling(none_stop=True)