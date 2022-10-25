"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

n = int(input('Введите натуральное число: '))
mass = []
count = 2
while count <= n:
    if n % count == 0:
        mass.append(count)
        n /= count
    else:
        count += 1

print(mass)