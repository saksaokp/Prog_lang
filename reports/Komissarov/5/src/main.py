import os
import csv
from pprint import pprint
from typing import List, Tuple, Union
Students = List[List[Union[str, int]]]
Header = List[str]

def save(filename: str, header, studentsTable) -> None:
    with open(filename, 'w', encoding='utf-8') as file: #Открытие файла filename на запись
        writer = csv.writer(file, delimiter=';', lineterminator='\n') #инициализируем csv.writer
        writer.writerows([header] + studentsTable) #запись элементов таблицы с помощью csv.writer, разделитель - ;
    print(' ')
    print_all(f'Сохранено в файл:', header, studentsTable)


def load(filename: str) -> Tuple[Header, Students]:
    with open(filename, 'r', encoding='utf-8') as file: #Открытие файла filename на чтение
        reader = csv.reader(file, delimiter=';') #инициализируем csv.reader
        studentsTable = list(reader) #чтение таблицы значений в список
        header = studentsTable.pop(0) #добавление шапки таблицы в начало списка
    for student in studentsTable: #расстановка значений по ячейкам таблицы
        student[0] = int(student[0]) 
        student[2] = int(student[2])
    print_all(f'Загружено из файла:', header, studentsTable)
    return header, studentsTable


def print_all(text: str, header, studentsTable) -> None:
    if text:print(text)
    if header:
        print('--------------------------')
        pprint(header)
    if studentsTable:pprint(studentsTable) #Pretty-print(pprint) позволяет "красиво" выводить списки значений в виде таблицы
    print('')


def menu(header, studentsTable) -> None:
    while True:
        print('Действия:')
        print('(1) Увеличить возраст студентов группы на 1')
        print('(2) Сохранить')
        print('(3) Сохранить в загруженный файл')
        print('(4) Открыть')
        print('(5) Выход из программы')
        act = input('Вариант действия: ')
        if act == '1':
            group = input('Возраст студентов какой группы вы хотите увеличить? ')
            increase(studentsTable, group)
        elif act == '2':
            filename = 'csv/' + input('Файл для сохранения: ')
            save(filename, header, studentsTable)
        elif act == '3':
            filename = 'csv/students.csv'
            save(filename, header, studentsTable)
        elif act == '4':
            header, studentsTable = load(input('Файл для открытия: csv/'))
        elif act == '5':
            return


def increase(studentsTable, group) -> None:
    print('...')
    for student in studentsTable:
        if (student[3] == group) : student[2] += 1
    print_all('', None, studentsTable)


def main():
    header, studentsTable = load('csv/students.csv')
    studentsTable.sort(key=lambda x: x[2])
    print_all(f'По возрасту студентов: ', header, studentsTable)
    menu(header, studentsTable)

main()
