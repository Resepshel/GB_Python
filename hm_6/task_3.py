"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

mass = [2, 3, 5, 9, 3, 6, 1, 3, 7]
result = 0

for el in range(len(mass)):
    if el % 2 != 0:
        result += mass[el]

print(result)
"""

mass = list(map(int, input('Введите числа, через пробел: ').split()))
# or mass = [el for el in range(10)]


result = 0

for el in range(len(mass)):
    if el % 2 != 0:
        result += mass[el]

print(result)
