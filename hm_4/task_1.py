"""
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

from math import pi
n = input('Введите точность (например, 0.001): ')
d = 0
if 1 < len(n)-2 < 11:
    for el in n[2:]:
        d += 1
else:
    d = 10
print(round(pi, d))
p = round(sum((1/(16**k))*((4/(8*k+1)) - (2/(8*k+4)) - (1/(8*k+5)) - (1/(8*k+6))) for k in range(d+1)), d)
print(p)
