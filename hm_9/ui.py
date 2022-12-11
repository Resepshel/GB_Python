from lot import lot_choise_func
from game import game


def create_and_refresh_board(board_func):
    for el in range(3):
        print('-------------')
        print('|', board_func[el][0], '|', board_func[el][1], '|', board_func[el][2], '|')
    print('-------------')


def init_game():
    symb = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    names = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
    create_and_refresh_board(symb)
    first_player, second_player = lot_choise_func(names)
    print(game(first_player, second_player, symb))
