"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
"""

import random

n = int(input('Введите число: '))
mass = []
with open('for_task_4.txt', 'w') as f:
    for el in range(n):
        f.write(f'{el}\n')
        number = random.randint(-n, n)
        mass.append(number)

print(f'Список чисел: {mass}')

first_num = random.choice(open('for_task_4.txt').readlines())
second_num = random.choice(open('for_task_4.txt').readlines())

print(f'Первая позиция: {first_num}Вторая позиция: {second_num}')

result = mass[int(first_num)] * mass[int(second_num)]

print(f'Произведение чисел на заданных позициях: {result}')
