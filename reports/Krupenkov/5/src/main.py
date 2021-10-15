from pprint import pprint
from typing import List, Tuple, Union
import csv

Header = List[str]
Students = List[List[Union[str, int]]]
Table = Tuple[Header, Students]


def load(filename: str) -> Table:
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        students = list(reader)
        header = students.pop(0)

    for student in students:
        student[0] = int(student[0])
        student[2] = int(student[2])

    print_all(f'Загружено из "{filename}":', header, students)
    return header, students


def print_all(text: str, header, students) -> None:
    if text:
        print(text)
    if header:
        print('Header:')
        pprint(header)
    if students:
        print('Students:')
        pprint(students)
    print()


def decrease(students) -> None:
    for student in students:
        student[2] -= 1
    print_all('\nУменьшено на 1:', None, students)


def save(filename, header, students) -> None:
    pprint(header)
    print(students)

    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\n')
        writer.writerows([header] + students)

    print_all(f'Сохранено в "{filename}":', header, students)


def menu(header, students) -> None:
    print('\nМеню:')
    print('1: Уменьшить возраст всех студентов на 1')
    print('2: Сохранить')
    print('3: Загрузить')
    print('0: Выход из программы')
    while True:
        inp = input('[MENU] Выберите вариант: ')
        if inp == '1':
            decrease(students)
        elif inp == '2':
            filename = 'files/' + input('Введите название файла для сохранения: ')
            save(filename, header, students)
        elif inp == '3':
            header, students = load(input('Введите название файла для загрузки: files/'))
        elif inp == '0':
            return


def main():
    header, students = load('files/students.csv')
    students.sort(key=lambda x: x[1])
    print_all(f'Отсортированная по фамилиям таблица: ', header, students)

    menu(header, students)


if __name__ == '__main__':
    main()
