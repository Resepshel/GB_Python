"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.
"""


def encode():
    with open('for_task_4_decode.txt') as dec:
        str_func = dec.read()
        print(str_func)
    result = ''
    count = 0
    for el in range(len(str_func)):
        if (el + 1) < len(str_func) and str_func[el] == str_func[el + 1]:
            count += 1
        elif (el + 1) < len(str_func) and str_func[el] != str_func[el + 1]:
            count += 1
            result += f'{count}{str_func[el]}'
            count = 0
        elif (el + 1) == len(str_func):
            count += 1
            result += f'{count}{str_func[el]}'

    with open('for_task_4_encode.txt', 'w') as enc:
        enc.write(result)


def decode():
    with open('for_task_4_encode.txt') as enc:
        str_func = enc.read()
        print(str_func)
    count = 0
    result = ''
    for el in range(len(str_func)):
        if str_func[el].isdigit():
            count = int(str_func[el])
        else:
            result += f'{str_func[el] * count}'

    with open('for_task_4_decode.txt', 'w') as dec:
        dec.write(result)


# str = 'AAAAABBCCCDD'
# encode()  # проверить чтобы в фале ..decode.txt находились не закодированные данные
decode()  # проверить чтобы в фале ..encode.txt находились закодированные данные

