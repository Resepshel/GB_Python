"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

mass = [0]
fib2 = count = 1
fib1 = 0
k = int(input('Введите число: '))

while count <= k:
    if count == 1:
        mass.append(fib2)
        mass.insert(0, fib2)
    elif count > 1:
        fib1, fib2 = fib2, fib1 + fib2
        mass.append(fib2)
        mass.insert(0, fib2 * ((-1)**(count+1)))
    count += 1

print(mass)
