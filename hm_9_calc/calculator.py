import re
import priority_complex
import priority_simple


def validation(string):
    # string = '4+3j*(3-7j+5j)'
    string = string.replace(" ", "")

    if 'j' in string or 'i' in string:
        result = complex_num(string)
    else:
        result = simple_num(string)

    return result


def simple_num(string):
    mass = re.findall(r'([()]|[0-9]+|[+\-*/])', string)

    while True:
        if '(' in mass and ')' in mass:
            mass = priority_simple.hooks(mass)
            continue
        if '*' in mass and '/' in mass:
            mass = priority_simple.mul_and_div(mass)
            continue
        elif '*' in mass or '/' in mass:
            mass = priority_simple.mul_or_div(mass)
            continue
        elif '+' in mass and '-' in mass:
            mass = priority_simple.sum_and_sub(mass)
            continue
        elif '+' in mass or '-' in mass:
            mass = priority_simple.sum_or_sub(mass)
        else:

            return mass


def complex_num(string):
    mass = re.findall(r'([()]|[0-9]+[+\-]{1}[0-9]+[ij]|[0-9]+[ij]|[0-9]+|[+\-*/])', string)

    while True:
        if '(' in mass and ')' in mass:
            mass = priority_complex.hooks(mass)
            continue
        if '*' in mass and '/' in mass:
            mass = priority_complex.mul_and_div(mass)
            continue
        elif '*' in mass or '/' in mass:
            mass = priority_complex.mul_or_div(mass)
            continue
        elif '+' in mass and '-' in mass:
            mass = priority_complex.sum_and_sub(mass)
            continue
        elif '+' in mass or '-' in mass:
            mass = priority_complex.sum_or_sub(mass)
        else:

            return mass
