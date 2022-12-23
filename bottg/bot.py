import telebot
import requests

bot = telebot.TeleBot('5955607703:AAHOZ0AYb-tLB9B6V2uCX9qvls9inHZzpls')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет. Напиши /help, чтобы узнать мои команды')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Чтобы получить фото, напиши /starts')

@bot.message_handler(commands=['starts'])
def starts(message):
    r = requests.get('http://thecatapi.com/api/images/get?format=src')
    url = r.url
    bot.send_photo(message.chat.id, url)



@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id," /help")
    else:
        bot.send_message(message.chat.id,"Напиши /help")



bot.polling(none_stop=True)
