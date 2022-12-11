def mul(mass, index):
    num1 = mass[index - 1]
    num2 = mass[index + 1]
    res = float(num1) * float(num2)
    del mass[index - 1:index + 2]
    mass.insert(index - 1, res)

    return mass


def div(mass, index):
    num1 = mass[index - 1]
    num2 = mass[index + 1]
    try:
        res = float(num1) / float(num2)
    except ZeroDivisionError:
        return "Ты делишь на 0! Так делать нельзя!"
    del mass[index - 1:index + 2]
    mass.insert(index - 1, res)

    return mass


def sum(mass, index):
    num1 = mass[index - 1]
    num2 = mass[index + 1]
    res = float(num1) + float(num2)
    del mass[index - 1:index + 2]
    mass.insert(index - 1, res)

    return mass


def sub(mass, index):
    num1 = mass[index - 1]
    num2 = mass[index + 1]
    res = float(num1) - float(num2)
    del mass[index - 1:index + 2]
    mass.insert(index - 1, res)

    return mass
