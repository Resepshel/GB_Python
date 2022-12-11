import csv


def exp_data(data):
    with open('log.csv', 'a', encoding='utf-8') as exp_f:
        file_writer = csv.writer(exp_f, delimiter=";", lineterminator='\n')
        file_writer.writerow(data)
