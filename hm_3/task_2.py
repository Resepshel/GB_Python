"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

mass = [2, 3, 4, 5, 6]
result = []
first = 0
last = -1

while first < len(mass)/2 and abs(last) < len(mass) + 1:
    result.append(mass[first] * mass[last])
    first += 1
    last -= 1

print(result)
