"""
Создайте программу для игры в ""Крестики-нолики"".
"""
from random import choice


def create_and_refresh_board(board_func):
    for el in range(3):
        print('-------------')
        print('|', board_func[el][0], '|', board_func[el][1], '|', board_func[el][2], '|')
    print('-------------')


def lot_choise_func(names_func):
    lot = ['X', 'O']
    lot_choice = choice(lot)
    if lot_choice == 'X':
        for el in names_func:
            yield el
    else:
        for el in names_func[::-1]:
            yield el


def check_bingo(sym):
    bingo = [
        [sym[0][0], sym[0][1], sym[0][2]],
        [sym[1][0], sym[1][1], sym[1][2]],
        [sym[2][0], sym[2][1], sym[2][2]],
        [sym[0][0], sym[1][0], sym[2][0]],
        [sym[0][1], sym[1][1], sym[2][1]],
        [sym[0][2], sym[1][2], sym[2][2]],
        [sym[0][0], sym[1][1], sym[2][2]],
        [sym[0][2], sym[1][1], sym[2][0]]
    ]
    for el in bingo:
        if el == ['X', 'X', 'X'] or el == ['O', 'O', 'O']:
            return False
    return True


def game(fp, sp, sym):
    flag = True
    turn = 0
    while flag:
        while True:
            turn_fp = input(f'Ходит {fp}\nВведите ряд и столбец (2 3): ').split()
            if len(turn_fp) != 2 or any([el not in ['1', '2', '3'] for el in turn_fp]):
                print('Вы ввели что-то не то!')
                continue
            else:
                r, c = turn_fp
                if sym[int(r)-1][int(c)-1] == 'X' or sym[int(r)-1][int(c)-1] == 'O':
                    print('Данная клетка занята!')
                    continue
                sym[int(r)-1][int(c)-1] = 'X'
                break

        create_and_refresh_board(sym)
        turn += 1
        if turn == 9:
            return f'Ничья'
        if turn > 4:
            flag = check_bingo(sym)
            if not flag:
                continue

        while True:
            turn_fp = input(f'Ходит {sp}\nВведите ряд и столбец (2 3): ').split()
            if len(turn_fp) != 2 or any([el not in ['1', '2', '3'] for el in turn_fp]):
                print('Вы ввели что-то не то!')
                continue
            else:
                r, c = turn_fp
                if sym[int(r)-1][int(c)-1] == 'X' or sym[int(r)-1][int(c)-1] == 'O':
                    print('Данная клетка занята!')
                    continue
                sym[int(r)-1][int(c)-1] = 'O'
                break

        create_and_refresh_board(sym)
        turn += 1
        if turn > 4:
            flag = check_bingo(sym)
            if not flag:
                continue

    if turn % 2 == 1:
        return f'Победил {fp}'
    elif turn % 2 == 0:
        return f'Победил {sp}'


symb = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
names = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
create_and_refresh_board(symb)
first_player, second_player = lot_choise_func(names)
print(game(first_player, second_player, symb))
