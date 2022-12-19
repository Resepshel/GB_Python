import calculate_complex


def hooks(mass):
    rev = list(reversed(mass))
    index_open = len(mass) - rev.index('(') - 1
    index_close = mass.index(')', index_open)
    sli = mass[index_open + 1:index_close]
    while True:
        if '*' in sli and '/' in sli:
            sli = mul_and_div(sli)
            continue
        elif '*' in sli or '/' in sli:
            sli = mul_or_div(sli)
            continue
        elif '+' in sli and '-' in sli:
            sli = sum_and_sub(sli)
            continue
        elif '+' in sli or '-' in sli:
            sli = sum_or_sub(sli)
            continue
        else:
            del mass[index_open:index_close+1]
            mass.insert(index_open, ''.join(map(str, sli)))

            return mass


def mul_and_div(mass):
    index_mul = mass.index('*')
    index_div = mass.index('/')
    if index_mul < index_div:
        mass = calculate_complex.mul(mass, index_mul)
    else:
        mass = calculate_complex.div(mass, index_div)

    return mass


def mul_or_div(mass):
    if '*' in mass:
        index_mul = mass.index('*')
        mass = calculate_complex.mul(mass, index_mul)
    else:
        index_div = mass.index('/')
        mass = calculate_complex.div(mass, index_div)

    return mass


def sum_and_sub(mass):
    index_sum = mass.index('+')
    index_sub = mass.index('-')
    if index_sum < index_sub:
        mass = calculate_complex.sum(mass, index_sum)
    else:
        mass = calculate_complex.sub(mass, index_sub)

    return mass


def sum_or_sub(mass):
    if '+' in mass:
        index_sum = mass.index('+')
        mass = calculate_complex.sum(mass, index_sum)
    else:
        index_sub = mass.index('-')
        mass = calculate_complex.sub(mass, index_sub)

    return mass