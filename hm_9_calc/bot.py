import telebot
from datetime import datetime
from calculator import validation
from logger import exp_data

bot = telebot.TeleBot("5931391196:AAFr7HWFXy6ulDQJCjh1Q70lA4AP04KYoZg")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Просто отправь мне пример и я его посчитаю!\nНапример, 4+3j*3-7j")


@bot.message_handler(content_types=['text'])
def user_text(message):
    date = datetime.now().strftime('%d-%m-%Y %H:%M')
    text = message.text
    res = validation(text)
    flag = isinstance(res, str)
    if not flag:
        for el in res:
            bot.reply_to(message, el)
            data_mass = [date, message.from_user.first_name, message.from_user.last_name, message.text, el]
            exp_data(data_mass)
    else:
        bot.reply_to(message, res)
        data_mass = [date, message.from_user.first_name, message.from_user.last_name, message.text, res]
        exp_data(data_mass)


bot.infinity_polling()
