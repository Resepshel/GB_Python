import csv


def imp_data(data):
    with open('Phonebook.csv', 'r', encoding='utf-8') as imp_f:
        for el in imp_f.readlines():
            if data in el:
                yield el


def exp_data(data):
    with open('Phonebook.csv', 'a', encoding='utf-8') as exp_f:
        file_writer = csv.writer(exp_f, delimiter=";", lineterminator='\n')
        file_writer.writerow(data)
