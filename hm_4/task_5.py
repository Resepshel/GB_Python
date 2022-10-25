"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""


def calc_degree_and_coeff(list_poly):
    values_poly_func = []
    signs_func = []
    for el in range(len(list_poly)):
        if list_poly[el].find('^') != -1:
            degree_func = int(list_poly[el][list_poly[el].find('^') + 1:])
            coeff_func = int(list_poly[el][:list_poly[el].find('x')])
            values_poly_func.append((degree_func, coeff_func))
        elif list_poly[el].find('^') == -1:
            if list_poly[el].find('x') != -1:
                degree_func = 1
                coeff_func = int(list_poly[el][:list_poly[el].find('x')])
                values_poly_func.append((degree_func, coeff_func))
            elif list_poly[el].find('x') == -1 and list_poly[el].find('+') == -1 and list_poly[el].find('-') == -1:
                degree_func = 0
                coeff_func = int(list_poly[el][:])
                values_poly_func.append((degree_func, coeff_func))
            else:
                signs_func.append(list_poly[el])

    return values_poly_func, signs_func


def insert_signs(list_poly, signs_func):
    if len(signs_func) < len(list_poly):
        for el in range(1, len(list_poly)):
            degree_func, coeff_func = list_poly[el]
            list_poly.pop(el)
            if signs_func[el - 1] == '+':
                list_poly.insert(el, (degree_func, coeff_func))
            else:
                list_poly.insert(el, (degree_func, -coeff_func))
    else:
        for el in range(len(list_poly)):
            degree_func, coeff_func = list_poly[el]
            list_poly.pop(el)
            if signs_func[el - 1] == '+':
                list_poly.insert(el, (degree_func, coeff_func))
            else:
                list_poly.insert(el, (degree_func, -coeff_func))

    return list_poly


def sum_poly(list_poly_1_func, list_poly_2_func):
    for i in range(len(list_poly_1_func)):
        for el in list_poly_2_func:
            if list_poly_1_func[i][0] == el[0]:
                list_poly_1_func[i] = (list_poly_1_func[i][0], (list_poly_1_func[i][1] + el[1]))
                list_poly_2_func.remove(el)

    sum = list_poly_1_func + list_poly_2_func

    for el in (sum):
        if el[1] == 0:
            sum.remove(el)

    return sum


with open('for_task_5_poly_1.txt') as f1:
    with open('for_task_5_poly_2.txt') as f2:
        f_poly_1 = f1.read()
        f_poly_2 = f2.read()
print(f'Первый многочлен: {f_poly_1}\nВторой многочлен: {f_poly_2}')
res_poly = ''
cut_poly_1 = f_poly_1[:f_poly_1.find('=')]
list_poly_1 = cut_poly_1.split()
cut_poly_2 = f_poly_2[:f_poly_2.find('=')]
list_poly_2 = cut_poly_2.split()

coeff, signs = calc_degree_and_coeff(list_poly_1)
list_poly_1 = insert_signs(coeff, signs)
coeff, signs = calc_degree_and_coeff(list_poly_2)
list_poly_2 = insert_signs(coeff, signs)
result = sum_poly(list_poly_1, list_poly_2)

for el in result:
    if el[0] > 1:
        if result.index(el) != 0 and el[1] > 0:
            res_poly += f' + {el[1]}x^{el[0]}'
        elif result.index(el) != 0:
            res_poly += f' - {abs(el[1])}x^{el[0]}'
        else:
            res_poly += f'{el[1]}x^{el[0]}'
    elif el[0] == 1:
        if result.index(el) != 0 and el[1] > 0:
            res_poly += f' + {el[1]}x'
        elif result.index(el) != 0:
            res_poly += f' - {abs(el[1])}x'
        else:
            res_poly += f'{el[1]}x^{el[0]}'
    elif el[0] == 0:
        if result.index(el) != 0 and el[1] > 0:
            res_poly += f' + {el[1]}x'
        elif result.index(el) != 0:
            res_poly += f' - {abs(el[1])}x'
        else:
            res_poly += f'{el[1]}x^{el[0]}'

res_poly += ' = 0'
print(res_poly)
with open('for_task_5_result.txt', 'w') as res:
    res.write(res_poly)
