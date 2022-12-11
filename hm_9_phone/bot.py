import telebot
from telebot import types
from operation import exp_data, imp_data

bot = telebot.TeleBot("5931391196:AAFr7HWFXy6ulDQJCjh1Q70lA4AP04KYoZg")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = types.KeyboardButton("Найти")
    button_2 = types.KeyboardButton("Добавить")
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, 'Привет! Я телефонный справочник',
                     reply_markup=markup)


@bot.message_handler(regexp='Найти')
def search_number(message):
    global flag
    flag = 'find'
    bot.send_message(message.chat.id, 'Введите фамилию контакта который хотите найти: ')


@bot.message_handler(regexp='Добавить')
def insert_number(message):
    global flag
    flag = 'insert'
    bot.reply_to(message, 'Введите фамилию и имя: ')


@bot.message_handler(content_types=['text'])
def user_text(message):
    global flag
    if flag == 'find':
        search = message.text
        data = imp_data(search)
        for el in data:
            sn, ln, pn, dp = el.split(';')
            bot.send_message(message.chat.id, f'{ln} {sn}\n{pn}\n{dp}')
        flag = ''
    elif flag == 'insert':
        surname, name = message.text.split(' ')
        mass_info.append(surname)
        mass_info.append(name)
        msg = bot.send_message(message.chat.id, 'Введите номер телефона: ')
        bot.register_next_step_handler(msg, f_phone_number)
    else:
        bot.send_message(message.chat.id, 'Выберите режим')


def f_phone_number(message):
    phone_number = message.text
    mass_info.append(phone_number)
    msg = bot.send_message(message.chat.id, 'Добавьте описание')
    bot.register_next_step_handler(msg, f_description)


def f_description(message):
    global flag
    description = message.text
    mass_info.append(description)
    exp_data(mass_info)
    flag = ''
    bot.send_message(message.chat.id, 'Контакт добавлен')


mass_info = []
flag = ''
bot.infinity_polling()
