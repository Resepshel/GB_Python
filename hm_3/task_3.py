"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

mass = [1.1, 1.2, 3.1, 5, 10.01]
minimum = 1
maximum = 0

new_mass = [round(el % 1, 3) for el in mass if el % 1 != 0]
print(new_mass)

# for el in new_mass:
#     if el >= maximum:
#         maximum = el
#     if el <= minimum:
#         minimum = el
#
# print(round(maximum - minimum, 3))
