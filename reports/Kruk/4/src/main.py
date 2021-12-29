import math
import random
import string

matrix_const = [[1, 2, 3, 4, 5, 6, 7, 8],
                [8, 7, 6, 5, 4, 3, 2, 1],
                [2, 3, 4, 5, 6, 7, 8, 9],
                [9, 8, 7, 6, 5, 4, 3, 2],
                [1, 3, 5, 7, 9, 7, 5, 3],
                [3, 1, 5, 3, 2, 6, 5, 7],
                [1, 7, 5, 9, 7, 3, 1, 5],
                [2, 6, 3, 5, 1, 7, 3, 2]]


def task1():
    a, b, c, d, f = int(input('a = ')), int(input('b = ')), int(input('c = ')), int(input('d = ')), int(input('f = '))
    res = math.fabs(a - b * c * d ** 3 + (c ** 5 - a ** 2) / a + f ** 3 * (a - 213)) if a != 0 else 0
    print(res)


def task2(l=[1, 'sad', 'asd', 32, '33', 534, 'trre']):
    print(f'Изначальный список: {l}')
    print(*l[1::2], sep=' ')


def task3(l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]):
    print(f'Изначальный список: {l}')
    output = 1
    for num in [x for x in l if x < 10]:
        output *= num
    print(output)


def task4(l=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(f'Изначальный список: {l}')
    print(l[len(l) // 2])


def task5():
    my_number = int(input('Введите число: '))
    user_number = my_number
    while user_number <= my_number:
        user_number = int(input('Введите число: '))


def task6(l=['rea', 'green', 'row', 'column', 'test']):
    print(f'Изначальный список: {l}')
    print(*[x for x in l if x.startswith('r')])


def task7():
    numbers = [str(random.choice(string.ascii_letters)) for _ in range(8)]
    if not any([x is int for x in numbers]):
        for _ in range(random.randint(1, 3)):
            numbers[random.randint(0, 7)] = str(random.randint(0, 9))
    output = ''.join(numbers)
    print(output)


def task8():
    s = input('Введите строку: ')
    new_s_dig = ''.join([x for x in s if x.isdigit()])
    new_s_let = ''.join([x for x in s if not x.isdigit()])

    print(new_s_dig)
    print(new_s_let)


def task9():
    matrix = matrix_const
    print('Изначальная матрица: ')
    print(*matrix, sep='\n')
    for row_index in range(4):
        for element_index in range(len(matrix[row_index])):
            matrix[row_index][element_index] **= 2
    print(*matrix, sep='\n')


def task10():
    matrix = matrix_const
    print('Изначальная матрица: ')
    print(*matrix, sep='\n')
    output_line = [item if item % 2 == 0 else 0 for item in matrix[0]]
    for line in matrix[1:]:
        for index, item in enumerate(line):
            output_line[index] += item if item % 2 == 0 else 0
    print('Результат: ')
    print(output_line)


def task11():
    matrix = matrix_const
    print('Изначальная матрица: ')
    print(*matrix, sep='\n')
    matrix = [[0] * len(matrix[0])] * len(matrix)
    print('Результат: ')
    print(*matrix, sep='\n')


def task12():
    matrix = matrix_const
    print('Изначальная матрица: ')
    print(*matrix, sep='\n')
    for row_index, line in enumerate(matrix):
        for col_index, element in enumerate(line):
            if element % 2 == 0:
                matrix[row_index][col_index] = 0
    print('Результат: ')
    print(*matrix, sep='\n')


def task13():
    matrix = matrix_const
    print('Изначальная матрица: ')
    print(*matrix, sep='\n')
    number = int(input('Введите номер строки для удаления: '))
    del matrix[number]
    print('Результат: ')
    print(*matrix, sep='\n')


def task14():
    matrix = matrix_const
    print('Изначальная матрица: ')
    print(*matrix, sep='\n')
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
    print('Результат: ')
    print(*matrix, sep='\n')


def task15():
    text = input('Введите текст: ')
    for chr in ',.:-;':
        text.replace(chr, '')
    output = ''
    for s in text.split(' '):
        if s.endswith('ов'):
            output += s + ' '
    print(output.strip())


def task16(students='Ф;И;О;Возраст;Категория;Иванов;Иван;Иванович;23 года;Студент 3 курас'):
    print('Изначальная строка: ' + students)
    str = '{0:<30}{1:>30}'
    splited = students.split(';')
    lastname = splited[::5]
    firstname = splited[1::5]
    fath = splited[2::5]
    age = splited[3::5]
    category = splited[4::5]
    category[0] = 'О Студенте'
    age[0] = ''

    for i in range(len(lastname)):
        print(str.format(lastname[i] + ' ' + firstname[i] + ' ' + fath[i], (category[i] + ', ' + age[i]).strip(', ')))


def task17(students='ФИО;Возраст;Категория;Аванов Аван Иванович;23 года;Студент'):
    print('Изначальная строка: ' + students)
    splited = students.split(';')
    output = '{0:30}{1:10}{2:15}'
    fullname = splited[::3]
    age = splited[1::3]
    category = splited[2::3]
    print(output.format(fullname[0], age[0], category[0]))
    for i in range(1, len(fullname)):
        if fullname[i].startswith('А') or fullname[i].startswith('Б'):
            print(output.format(fullname[i], age[i], category[i]))


def task18():
    s = input('Введите строку: ')
    print(len(s))
    print(len(s.split()))


def task19():
    matrix = matrix_const
    print('Изначальная матрица: ')
    print(*matrix, sep='\n')
    s = 0
    for line in matrix:
        s += sum(line)
    print(s)


def task20(l=[1, 2, 3, 4, 5, 65, 23, 65, 12, 122]):
    print(f'Изначальный список: {l}')
    print([x for x in l if x % 2 != 0] + [1, 2, 3, 4, 5])
    l = l[1::2] + [1, 2, 3, 4, 5]
    print(l)


def task21(l=[['БОoup', ['1', '2', '3', '4', '5']], ['БОdsa', ['12', '123', '213']]]):
    print(f'Изначальный список: {l}')
    for group in l:
        if group[0].startswith('БО'):
            print(f'{group[0]}: ' + ', '.join(group[1]))


def task22(l=[['БОoup', ['А П', 'П А', 'ПП АА']], ['БОdsa', ['12', '123', '213']]]):
    print(f'Изначальный список: {l}')
    for group in l:
        print(group[0], end=': ')
        print(*group[1][::2], sep=', ')


def menu():
    options = {
        1: task1,
        2: task2,
        3: task3,
        4: task4,
        5: task5,
        6: task6,
        7: task7,
        8: task8,
        9: task9,
        10: task10,
        11: task11,
        12: task12,
        13: task13,
        14: task14,
        15: task15,
        16: task16,
        17: task17,
        18: task18,
        19: task19,
        20: task20,
        21: task21,
        22: task22
    }

    print('0-Выход')
    for num in range(1, 23):
        print(f'{num}. Задание {num}')
    choise = int(input('Ваш выбор: '))

    if choise > 0:
        options[choise]()

    print('Вы хотете продолжить?\nYes/No')
    if input() == 'Y':
        menu()


if __name__ == '__main__':
    menu()
