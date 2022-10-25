"""
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
последовательности.
"""

from random import randint

mass = [randint(1, 6) for el in range(7)]
print(mass)
result = []

for el in mass:
    counter = mass.count(el)
    if counter == 1:
        result.append(el)
    else:
        continue

print(result)
