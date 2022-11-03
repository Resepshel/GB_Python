"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""
from random import choice, randint


def lot_choise_func(names_func):
    lot = [1, 2]
    lot_choice = choice(lot)
    if lot_choice == 1:
        for el in names_func:
            yield el
    else:
        for el in names_func[::-1]:
            yield el


def player_vs_player(candies_func, max_per_turn):
    names = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
    first_player, second_player = lot_choise_func(names)

    while candies_func > 0:
        while True:
            turn_first_player = int(input(f'Ходит {first_player}: '))
            if 1 <= turn_first_player <= max_per_turn:
                candies_func -= turn_first_player
                print(f'Конфет осталось: {candies_func}')
                break
            else:
                print('Введено недопустимое кол-во конфет!')
                continue
        if candies_func <= 0:
            return f'{first_player} победил!'
        while True:
            turn_second_player = int(input(f'Ходит {second_player}: '))
            if 1 <= turn_second_player <= max_per_turn:
                candies_func -= turn_second_player
                print(f'Конфет осталось: {candies_func}')
                break
            else:
                print('Введено недопустимое кол-во конфет!')
                continue
        if candies_func <= 0:
            return f'{second_player} победил!'


def player_vs_bot(candies_func, max_per_turn):
    names = [input('Введите имя игрока: '), 'BOT']
    first_player, second_player = lot_choise_func(names)

    while candies_func > 0:
        while True:
            if first_player == 'BOT':
                if candies_func <= 28:
                    turn_bot = candies_func
                else:
                    turn_bot = randint(1, max_per_turn)
                print(f'Ходит {first_player}: {turn_bot}')
                candies_func -= turn_bot
                print(f'Конфет осталось: {candies_func}')
                break
            elif first_player != 'BOT':
                turn_player = int(input(f'Ходит {first_player}: '))
                if 1 <= turn_player <= max_per_turn:
                    candies_func -= turn_player
                    print(f'Конфет осталось: {candies_func}')
                    break
                else:
                    print('Введено недопустимое кол-во конфет!')
                    continue
        if candies_func <= 0:
            return f'{first_player} победил!'
        while True:
            if second_player == 'BOT':
                if candies_func <= 28:
                    turn_bot = candies_func
                else:
                    turn_bot = randint(1, max_per_turn)
                print(f'Ходит {second_player}: {turn_bot}')
                candies_func -= turn_bot
                print(f'Конфет осталось: {candies_func}')
                break
            elif second_player != 'BOT':
                turn_player = int(input(f'Ходит {second_player}: '))
                if 1 <= turn_player <= max_per_turn:
                    candies_func -= turn_player
                    print(f'Конфет осталось: {candies_func}')
                    break
                else:
                    print('Введено недопустимое кол-во конфет!')
                    continue
        if candies_func <= 0:
            return f'{second_player} победил!'


def player_vs_ai(candies_func, max_per_turn):
    names = [input('Введите имя игрока: '), 'AI']
    first_player, second_player = lot_choise_func(names)

    while candies_func > 0:
        while True:
            if first_player == 'AI':
                turn_ai = candies_func - (candies_func // (max_per_turn+1)) * (max_per_turn+1)
                if turn_ai == 0:
                    turn_ai += 1
                elif turn_ai == 29:
                    turn_ai -= 1
                print(f'Ходит {first_player}: {turn_ai}')
                candies_func -= turn_ai
                print(f'Конфет осталось: {candies_func}')
                break
            elif first_player != 'AI':
                turn_player = int(input(f'Ходит {first_player}: '))
                if 1 <= turn_player <= max_per_turn:
                    candies_func -= turn_player
                    print(f'Конфет осталось: {candies_func}')
                    break
                else:
                    print('Введено недопустимое кол-во конфет!')
                    continue
        if candies_func <= 0:
            return f'{first_player} победил!'
        while True:
            if second_player == 'AI':
                turn_ai = candies_func - (candies_func // (max_per_turn+1)) * (max_per_turn+1)
                if turn_ai == 0:
                    turn_ai += 1
                elif turn_ai == 29:
                    turn_ai -= 1
                print(f'Ходит {second_player}: {turn_ai}')
                candies_func -= turn_ai
                print(f'Конфет осталось: {candies_func}')
                break
            elif second_player != 'AI':
                turn_player = int(input(f'Ходит {second_player}: '))
                if 1 <= turn_player <= max_per_turn:
                    candies_func -= turn_player
                    print(f'Конфет осталось: {candies_func}')
                    break
                else:
                    print('Введено недопустимое кол-во конфет!')
                    continue
        if candies_func <= 0:
            return f'{second_player} победил!'


candies = 2021
max_cand_per_turn = 28

# print(player_vs_player(candies, max_cand_per_turn))
# print(player_vs_bot(candies, max_cand_per_turn))
print(player_vs_ai(candies, max_cand_per_turn))