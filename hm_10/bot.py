import telebot
from telebot import types
import game
from random import randint

bot = telebot.TeleBot("token")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = types.KeyboardButton("Начать игру")
    button_2 = types.KeyboardButton("Правила")
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, 'Привет! Поиграем?\nЧтобы узнать правила игры просто нажми кнопку "Правила"',
                     reply_markup=markup)


@bot.message_handler(regexp='Начать игру')
def start_game(message):
    global stash
    stash = 200
    bot.send_message(message.chat.id, f'Вы ходите первым. Введите кол-во конфет которое хотите взять')


@bot.message_handler(regexp='Правила')
def rules(message):
    bot.reply_to(message, "На столе лежит 200 конфет. Вы играете против бота, делая ход друг после друга."
                          "За один ход можно забрать не более чем 28 конфет."
                          "Все конфеты оппонента достаются сделавшему последний ход.")


@bot.message_handler(content_types=['text'])
def user_text(message):
    global stash

    try:
        data = int(message.text)
        if data < 1 or data > 28:
            bot.send_message(message.chat.id, 'Вы взяли неверное число конфет')
            return
    except ValueError:
        bot.send_message(message.chat.id, 'Введите число')

    stash -= data
    bot.send_message(message.chat.id, f'{message.from_user.first_name} взял {data} конфет. В сундуке осталось {stash} конфет')

    if game.winner(stash):
        bot.send_message(message.chat.id, f'Победил бот!')
        return

    bot.send_message(message.chat.id, f'Следующий ходит бот')
    data = randint(1, 29)

    stash -= data
    bot.send_message(message.chat.id, f'Бот взял {data} конфет. В сундуке осталось {stash} конфет')

    if game.winner(stash):
        bot.send_message(message.chat.id, f'Победил {message.from_user.first_name}!')
        return


stash = 200
bot.infinity_polling()
