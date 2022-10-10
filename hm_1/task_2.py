"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""

x = False
y = False
z = False

left = not (x or y or z)
right = (not x) and (not y) and (not z)

if left == right:
    print('Ч.т.д.')
else:
    print('(')
