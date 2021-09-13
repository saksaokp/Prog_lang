from pprint import pprint
from typing import List, Optional


def printing(text=None, header=None, students=None):
    if text:
        print(text)
    if header:
        print('Header:')
        pprint(header)
    if students:
        print('Students:')
        pprint(students)


def load(filename):
    with open('files/' + filename, 'r', encoding='utf-8') as file:
        students: List[List[Optional[str, int]]] = []
        for line in file.read().split('\n'):
            students.append(line.split(';'))
    header = students.pop(0)
    for student in students:
        student[0] = int(student[0])
        student[2] = int(student[2])
    students.sort(key=lambda x: x[1])
    printing(f'Loaded from {filename}:', header, students)
    return header, students


def decrease(students):
    for student in students:
        student[2] -= 1
    printing('Decreased:', None, students)


def save(filename, header, students):
    # filename = 'new_students.csv'
    to_save: str = ''
    row_sep = ''
    for student in [header] + students:
        to_save += row_sep
        row_sep = '\n'
        val_sep = ''
        for i in student:
            to_save += val_sep + str(i)
            val_sep = ';'
    with open('files/' + filename, 'w', encoding='utf-8') as file:
        file.write(to_save)
    printing(f'Saved to {filename}:', header, students)


def menu(header, students):
    while True:
        print('\nMenu:')
        print('1: Уменьшить возраст всех студентов на 1')
        print('2: Сохранить')
        print('3: Загрузить')
        print('0: Выход из программы')
        inp = input()
        if inp == '1':
            decrease(students)
        elif inp == '2':
            save(input('Введите название файла для сохранения: '), header, students)
        elif inp == '3':
            load(input('Введите название файла для загрузки: '))
        elif inp == '0':
            break


def main():
    header, students = load('students.csv')
    menu(header, students)


if __name__ == '__main__':
    main()
