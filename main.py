from application.salary import calculate_salary
from application.db.people import list_of_jobs
import os
from datetime import datetime

if __name__ == '__main__':
    print(f'Добрый сегодня: {datetime.date(datetime.today())}')
    command = None
    while command != 'q':
        command = input('Введите команду - l - Список сотрудников, q - выход из программы: ')
        if command == 'l':
            file = os.path.join(os.getcwd(), 'base.xlsx')
            list_of_jobs(file)
            print('_______________________')
            number_worker = int(input('Введите номер работника, чтобы получить его заработную плату: '))
            calculate_salary(file, number_worker)










