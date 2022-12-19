# def lot_choise_func(names_func):
#     lot = [1, 2]
#     lot_choice = choice(lot)
#     if lot_choice == 1:
#         for el in names_func:
#             yield el
#     else:
#         for el in names_func[::-1]:
#             yield el


def winner(stash):
    if stash < 29:
        return True
    else:
        return False


# def player_vs_bot(candies_func, max_per_turn):
#     names = [input('Введите имя игрока: '), 'BOT']
#     first_player, second_player = lot_choise_func(names)
#
#     while candies_func > 0:
#         while True:
#             if first_player == 'BOT':
#                 if candies_func <= 28:
#                     turn_bot = candies_func
#                 else:
#                     turn_bot = randint(1, max_per_turn)
#                 print(f'Ходит {first_player}: {turn_bot}')
#                 candies_func -= turn_bot
#                 print(f'Конфет осталось: {candies_func}')
#                 break
#             elif first_player != 'BOT':
#                 turn_player = int(input(f'Ходит {first_player}: '))
#                 if 1 <= turn_player <= max_per_turn:
#                     candies_func -= turn_player
#                     print(f'Конфет осталось: {candies_func}')
#                     break
#                 else:
#                     print('Введено недопустимое кол-во конфет!')
#                     continue
#         if candies_func <= 0:
#             return f'{first_player} победил!'
#         while True:
#             if second_player == 'BOT':
#                 if candies_func <= 28:
#                     turn_bot = candies_func
#                 else:
#                     turn_bot = randint(1, max_per_turn)
#                 print(f'Ходит {second_player}: {turn_bot}')
#                 candies_func -= turn_bot
#                 print(f'Конфет осталось: {candies_func}')
#                 break
#             elif second_player != 'BOT':
#                 turn_player = int(input(f'Ходит {second_player}: '))
#                 if 1 <= turn_player <= max_per_turn:
#                     candies_func -= turn_player
#                     print(f'Конфет осталось: {candies_func}')
#                     break
#                 else:
#                     print('Введено недопустимое кол-во конфет!')
#                     continue
#         if candies_func <= 0:
#             return f'{second_player} победил!'


# candies = 2021
# max_cand_per_turn = 28

# print(player_vs_player(candies, max_cand_per_turn))
# print(player_vs_bot(candies, max_cand_per_turn))
# print(player_vs_ai(candies, max_cand_per_turn))
