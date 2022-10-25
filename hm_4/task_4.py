"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
from random import randint

poly = ''
count = 0
k = int(input(': '))
list_coeff = [randint(0, 100) for el in range(k+1)]
degree = k
print(list_coeff)
while count <= k:
    if 1 < degree <= k and list_coeff[count] not in (0, 1):
        poly += f'{list_coeff[count]}*x^{degree}'
        if list_coeff[count+1] != 0:
            poly += ' + '
    elif degree == 1 and list_coeff[count] not in (0, 1):
        poly += f'{list_coeff[count]}*x'
        if list_coeff[count+1] != 0:
            poly += ' + '
    elif degree == 0 and list_coeff[count] != 0:
        poly += f'{list_coeff[count]}'
    elif degree == k and list_coeff[count] == 0:
        poly += f'x^{degree}'
        if list_coeff[count+1] != 0:
            poly += ' + '
    elif degree != 0 and list_coeff[count] == 1:
        poly += f'x^{degree}'
        if list_coeff[count+1] != 0:
            poly += ' + '
    elif list_coeff[count] == 0:
        if list_coeff[count+1] != 0:
            poly += ' + '

    degree -= 1
    count += 1

poly += ' = 0'
with open('for_task_4.txt', 'w') as f:
    f.write(poly)
