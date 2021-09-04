from random import choice
from copy import deepcopy


def z1_1():
    a, b, c, k = map(int, input('\nЗадание 1 №1\na, b, c, k: ').split())
    if (a == 0) or (b == 0):
        print('Error (~/0)')
    else:
        result = abs((a ** 2 / b ** 2 + c ** 2 * a ** 2) / (a + b + c * (k - a / b ** 3)) + c + (k / b - k / a) * c)
        print(result)


def z1_2():
    list = [2, 5, 'sus', 16, '4', 3, 1]
    print('\nЗадание 1 №2\nlist: ', list)
    for el in list:
        try:
            if el % 2 == 0:
                print(el, ' ')
        except TypeError:
            continue


def z1_3():
    list = [2, 40, 23, 12, 9, 10, 6, 100]
    print('\nЗадание 1 №3\nlist: ', list)
    sum = 0
    for el in list:
        if el > 10:
            sum += el
    print('sum(>10): ', sum)


def z1_4():
    list = [2, 40, 23, 12, 9, 10, 6, 100]
    print('\nЗадание 1 №4\nlist: ', list)
    max = list[0]
    for el in list[1:]:
        if el > max:
            max = el
    print('max: ', max)


def z2_1():
    my_number = 2
    user_number = int(input('\nЗадание 2 №1\nuser_number: '))
    while user_number >= my_number:
        user_number = int(input('user_number: '))


def z2_2():
    list = input('\nЗадание 2 №2\ninput: ').split()
    print(list)
    for el in list:
        if 5 <= len(el) <= 10:
            print(el)


def z2_3():
    print('\nЗадание 2 №3')
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    for i in range(5):
        print(choice(alphabet), end='')


def z2_4():
    str = input('\nЗадание 2 №4\nВедите строку: ')
    new_str = ''
    for symbol in str:
        if symbol.isdigit():
            new_str += symbol
    print(new_str)


MATRIX = [[1, 2, 3, 4, 5, 6, 7, 8],
          [8, 7, 6, 5, 4, 3, 2, 1],
          [2, 3, 4, 5, 6, 7, 8, 9],
          [9, 8, 7, 6, 5, 4, 3, 2],
          [1, 3, 5, 7, 9, 7, 5, 3],
          [3, 1, 5, 3, 2, 6, 5, 7],
          [1, 7, 5, 9, 7, 3, 1, 5],
          [2, 6, 3, 5, 1, 7, 3, 2]]


# print('\nMATRIX:', *MATRIX, sep='\n')


def z3_1():
    matrix = deepcopy(MATRIX)
    for i in matrix:
        for j in range(len(i)):
            i[j] *= i[j]
    print('\nЗадание 3 №1', *matrix, sep='\n')


def z3_2():
    line = deepcopy(MATRIX[0])
    for i in MATRIX[1:]:
        for j in range(len(i)):
            line[j] += i[j]
    print('\nЗадание 3 №2', line, sep='\n')


def z3_4():
    line = deepcopy(MATRIX[0])
    for i in MATRIX[1:]:
        for j in range(len(i)):
            line[j] *= i[j]
    print('\nЗадание 3 №4', line, sep='\n')


def z3_5():
    matrix = deepcopy(MATRIX)
    for i in matrix:
        for j in range(len(i)):
            if i[j] % 2 == 0:
                i[j] *= 0
    print('\nЗадание 3 №5', *matrix, sep='\n')


def z3_6():
    matrix = deepcopy(MATRIX)
    delele_line = int(input('\nЗадание 3 №6\nВведите число: '))
    matrix.pop(delele_line)
    print(*matrix, sep='\n')


def z3_7():
    matrix = deepcopy(MATRIX)
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
    print('\nЗадание 3 №7', *matrix, sep='\n')


def z3_8():
    matrix = deepcopy(MATRIX)
    line = int(input('\nЗадание 3 №7\nСтрока матрицы: '))
    column = int(input('Столбец матрицы: '))
    print(matrix[column][line])


def z4_1():
    str = input('\nЗадание 4 №1\nПредложение: ').split()
    for el in str:
        if len(el) > 5:
            print(el, end=' ')


MY_STRING = 'Ф;И;О;Возраст;Категория;' \
            '_Иванов;Иван;Иванович;23 года;Студент 3 курса;' \
            '_Петров;Семен;Игоревич;22 года;Студент 2 курса' \
            '_Петров;Семен;Семенович;21 года;Студент 1 курса'


# print(f'\nMY_STRING:\n{MY_STRING}')


def z4_2():
    str = MY_STRING.split('_')
    for i in range(len(str)):
        str[i] = str[i].split(';')
    # print(str)
    print('\nЗадание 4 №2\nФИО                  \tКатегория        \tВозраст')
    for el in str[1:]:
        print(f'{el[0]} {el[1]} {el[2]} \t{el[4]} \t{el[3]}')


def z4_3():
    str = MY_STRING.split('_')
    for i in range(len(str)):
        str[i] = str[i].split(';')
    # print(str)
    print('\nЗадание 4 №3\nФИО                  \tКатегория        \tВозраст')
    for el in str[1:]:
        if el[0] == 'Петров':
            print(f'{el[0]} {el[1]} {el[2]} \t{el[4]} \t{el[3]}')


def z4_4():
    str = 'Это предложение здесь создано от безысходности.'
    print('\nЗадание 4 №4\nПредложение:', str)
    print(f'Количесто символов: {len(str)}\nКоличесто слов: {len(str.split())}')


def z6_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('\nЗадание 6 №1\nМатрица:', *matrix, sep='\n')
    list = []
    for el in matrix:
        for i in el:
            list.append(i)
    print('Конечный список:', list, sep='\n')


def z6_2():
    matrix = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('\nЗадание 6 №2\nНачальный список:', matrix, sep='\n')
    matrix.pop(0)
    matrix.pop(0)
    matrix.append(10)
    matrix.append(11)
    print('Конечный список:', matrix, sep='\n')


MY_LEN = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения']],
          ['БОВ-421102', ['Дедушкин Даниил', 'Небесный Дмитрий']],
          ['БО-331103', ['Апрошедший Александр']]]
print('\nMY_LEN:', *MY_LEN, sep='\n')


def z6_3():
    print('\nЗадание 6 №3')
    for el in MY_LEN:
        print(el[0])
        for i in el[1]:
            print(f'\t{i}')


def z6_4():
    print('\nЗадание 6 №4')
    for el in MY_LEN:
        for i in el[1]:
            if i[0] == 'А' or i[0] == 'A':  # Русская и английская
                print(f'{i} ({el[0]})')


# z1_1()
# z1_2()
# z1_3()
# z1_4()
# z2_1()
# z2_2()
# z2_3()
# z2_4()
# z3_1()
# z3_2()
# z3_4()
# z3_5()
# z3_6()
# z3_7()
# z3_8()
# z4_1()
# z4_2()
# z4_3()
# z4_4()
# z6_1()
# z6_2()
# z6_3()
# z6_4()
