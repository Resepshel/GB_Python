"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите координату x первой точки: '))
y1 = int(input('Введите координату y первой точки: '))
x2 = int(input('Введите координату x второй точки: '))
y2 = int(input('Введите координату y второй точки: '))

print(f'Расстояние между двумя точками = {((x1 - x2)**2 + (y1 - y2)**2)**0.5}')
"""

result = lambda x1, x2, y1, y2: ((x1 - x2)**2 + (y1 - y2)**2)**0.5

x1 = int(input('Введите координату x первой точки: '))
y1 = int(input('Введите координату y первой точки: '))
x2 = int(input('Введите координату x второй точки: '))
y2 = int(input('Введите координату y второй точки: '))

print(f'Расстояние между двумя точками = {result(x1, x2, y1, y2)}')
