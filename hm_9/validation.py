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