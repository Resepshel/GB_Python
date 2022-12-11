"""
Создайте программу для игры в ""Крестики-нолики"".
"""
from ui import create_and_refresh_board
from validation import check_bingo


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
