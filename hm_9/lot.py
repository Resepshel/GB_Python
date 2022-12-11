from random import choice


def lot_choise_func(names_func):
    lot = ['X', 'O']
    lot_choice = choice(lot)
    if lot_choice == 'X':
        for el in names_func:
            yield el
    else:
        for el in names_func[::-1]:
            yield el
