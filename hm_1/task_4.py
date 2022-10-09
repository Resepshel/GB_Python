"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""

quarter = int(input('Введите четверть: '))

if quarter == 1:
    print('x(0, inf); y(0, inf)')
elif quarter == 2:
    print('x(0, -inf); y(0, inf)')
elif quarter == 3:
    print('x(0, -inf); y(0, -inf)')
elif quarter == 4:
    print('x(0, inf); y(0, -inf)')
else:
    print('Существует всего 4 четверти')
