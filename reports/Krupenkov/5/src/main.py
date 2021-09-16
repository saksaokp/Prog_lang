from pprint import pprint
from typing import List, Tuple, Union

Header = List[str]
Students = List[List[Union[str, int]]]


def printing(text: str, header, students) -> None:
    if text:
        print(text)
    if header:
        print('Header:')
        pprint(header)
    if students:
        print('Students:')
        pprint(students)


def load(filename: str) -> Tuple[Header, Students]:
    filename = 'files/' + filename
    with open(filename, 'r', encoding='utf-8') as file:
        students: Students = []
        for line in file.read().split('\n'):
            students.append(line.split(';'))

    header: Header = students.pop(0)
    for student in students:
        student[0] = int(student[0])
        student[2] = int(student[2])
    students.sort(key=lambda x: x[1])
    printing(f'Загружено из "{filename}":', header, students)
    return header, students


def decrease(students) -> None:
    for student in students:
        student[2] -= 1
    printing('\nУменьшено на 1:', None, students)


def save(filename, header, students) -> None:
    filename = 'files/' + filename
    to_save: str = ''
    row_sep = ''
    for student in [header] + students:
        to_save += row_sep
        row_sep = '\n'
        val_sep = ''
        for i in student:
            to_save += val_sep + str(i)
            val_sep = ';'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(to_save)
    printing(f'Сохранено в "{filename}":', header, students)


def menu(header, students) -> None:
    while True:
        print('\nМеню:')
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
            header, students = load(input('Введите название файла для загрузки: '))
        elif inp == '0':
            return


def main():
    header, students = load('students.csv')
    menu(header, students)


if __name__ == '__main__':
    main()
