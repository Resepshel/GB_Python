"""
Реализуйте алгоритм перемешивания списка
"""
from random import randint

result = []
mass = [randint(-10, 10) for _ in range(20)]
print(mass)

for el in range(len(mass)):
    ind_rand = randint(0, len(mass)-1)
    result.append(mass[ind_rand])

print(result)
