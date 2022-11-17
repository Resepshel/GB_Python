from operation import imp_data
from operation import exp_data


def choice_format():
    while True:
        cho_for = input('Для импорта данных введите "И". Для экспорта данных введите "Э": ')
        if cho_for.upper() in 'И':
            search = input('Введите фамилию контакта который хотите найти: ')
            print('\n')
            compl = imp_data(search)
            for el in compl:
                sn, ln, pn, dp = el.split(';')
                print(f"Фамилия и имя: {sn} {ln}\nТелефон: {pn}\nОписание: {dp}")
        elif cho_for.upper() in 'Э':
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone_number = input("Введите номер телефона: ")
            description = input("Расскажите что-нибудь о себе: ")
            mass_info = [surname, name, phone_number, description]
            exp_data(mass_info)
        break
