from random import choice
from copy import deepcopy
from pprint import pprint
from typing import List, Union


def task1_1() -> None:
    print('\nЗадание 1.1 - решение формулы по введенным числам')
    a, b, c, k = map(float, input('a, b, c, k (через пробел): ').split())
    try:
        result = abs((a ** 2 / b ** 2 + c ** 2 * a ** 2) / (a + b + c * (k - a / b ** 3)) + c + (k / b - k / a) * c)
        print(result)
    except ZeroDivisionError:
        print('ZeroDivisionError')


def task1_2() -> None:
    print('\nЗадание 1.2 - вывод четных элементов')
    _list = [2, 5, 'sus', 16, '4', 3, 1]
    print(f'list: {_list}')
    for i, el in enumerate(_list):
        if i % 2:
            print(el)


def task1_3() -> None:
    print('\nЗадание 1.3 - сложение чисел списка больше 10')
    _list = [2, 40, 23, 12, 9, 10, 6, 100]
    print('list: ', _list)
    _sum = 0
    for el in _list:
        if el > 10:
            _sum += el
    print('sum(>10): ', _sum)


def task1_4() -> None:
    print('\nЗадание 1.4 - поиск максимального элемента в списке')
    _list = [2, 40, 23, 12, 9, 10, 6, 100]
    print('list: ', _list)
    _max = _list[0]
    for el in _list[1:]:
        if el > _max:
            _max = el
    print('max: ', _max)


def task2_1() -> None:
    print('\nЗадание 2.1 - запрос числа, пока оно не будет меньше  my_number (5)')
    my_number = 5
    user_number = int(input('user_number: '))
    while user_number >= my_number:
        user_number = int(input('user_number: '))


def task2_2() -> None:
    print('\nЗадание 2.2 - вывод строк списка размером от 5 до 10')
    _list = input('Список строк (через пробел): ').split()
    print(_list)
    for el in _list:
        if 5 <= len(el) <= 10:
            print(el)


def task2_3() -> None:
    print('\nЗадание 2.3 - вывод случайной строки из 5 заглавных букв русского алфавита')
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    for i in range(5):
        print(choice(alphabet), end='')
    print()


def task2_4() -> None:
    print('\nЗадание 2.4 - из строки сформировать новую из цифр')
    _str = input('Ведите строку: ')
    new_str = ''
    for symbol in _str:
        if symbol.isdigit():
            new_str += symbol
    print(f'Новая строка: {new_str}')


MATRIX: List[List[int]] = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2]
]


def task3_1() -> None:
    print('\nЗадание 3.1 - возведение всех элементов в квадрат')
    matrix = deepcopy(MATRIX)
    for i in matrix:
        for j in range(len(i)):
            i[j] *= i[j]
    print(*matrix, sep='\n')


def task3_2() -> None:
    print('\nЗадание 3.2 - сложение по строкам')
    line: List[int] = []
    for i in range(len(MATRIX)):
        line.append(sum(MATRIX[i]))
    print(line)


def task3_4() -> None:
    print('\nЗадание 3.4 - умножение по строкам')
    line = deepcopy(MATRIX[0])
    for i in MATRIX[1:]:
        for j in range(len(i)):
            line[j] *= i[j]
    print(line)


def task3_5() -> None:
    print('\nЗадание 3.5 - замена всех четных элементов на 0')
    matrix = deepcopy(MATRIX)
    for i in matrix:
        for j in range(len(i)):
            if i[j] % 2 == 0:
                i[j] *= 0
    print(*matrix, sep='\n')


def task3_6() -> None:
    print('\nЗадание 3.6 - удаление строки по введенному номеру')
    matrix = deepcopy(MATRIX)
    del_line = int(input('Введите номер (с нуля): '))
    matrix.pop(del_line)
    print(*matrix, sep='\n')


def task3_7() -> None:
    print('\nЗадание 3.7 - замена первой и последней строки')
    matrix = deepcopy(MATRIX)
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
    print(*matrix, sep='\n')


def task3_8() -> None:
    print('\nЗадание 3.8 - поиск по координатам')
    matrix = deepcopy(MATRIX)
    column = int(input('Столбец матрицы (с единицы): x = '))
    line = int(input('Строка матрицы (с единицы):  y = '))
    print(matrix[line - 1][column - 1])


def task4_1() -> None:
    print('\nЗадание 4.1 - Оставить в предложении только слова с более 5 буквами')
    _str = input('Введите предложение: ').split()
    for el in _str:
        if len(el) > 5:
            print(el, end=' ')


MY_STRING: str = 'Ф;И;О;Возраст;Категория;' \
                 '_Иванов;Иван;Иванович;23 года;Студент 3 курса;' \
                 '_Петров;Семен;Игоревич;22 года;Студент 2 курса;' \
                 '_Петров;Семен;Семенович;21 года;Студент 1 курса'
STR_LIST: List[str] = MY_STRING.split(';_')
STR_MATRIX: List[List[str]] = []
for el in STR_LIST:
    STR_MATRIX.append(el.split(';'))


def task4_2() -> None:
    print('\nЗадание 4.2 - красиво вывести MY_STRING')
    print('ФИО                  \tКатегория        \tВозраст')
    for el in STR_MATRIX[1:]:
        print(f'{el[0]} {el[1]} {el[2]} \t{el[4]} \t{el[3]}')


def task4_3() -> None:
    print('\nЗадание 4.3 - красиво вывести Петровых')
    print('ФИО                  \tКатегория        \tВозраст')
    for el in STR_MATRIX[1:]:
        if el[0] == 'Петров':
            print(f'{el[0]} {el[1]} {el[2]} \t{el[4]} \t{el[3]}')


def task4_4() -> None:
    print('\nЗадание 4.4 - вывести количество символов и слов')
    line = 'Это предложение здесь создано от безысходности.'
    print('Предложение:', line)
    print(f'Количесто символов: {len(line)}\nКоличесто слов: {len(line.split())}')


def task6_1() -> None:
    print('\nЗадание 6.1 - представить матрицу N*N в виде списка')
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('Матрица:', *matrix, sep='\n')
    matrix_list = []
    for el in matrix:
        for i in el:
            matrix_list.append(i)
    print('Конечный список:', matrix_list, sep='\n')
    print('Сумма всех элементов:', sum(matrix_list))


def task6_2() -> None:
    print('\nЗадание 6.2 - пусть дан список из 10 элементов, удавить 2 первых элемента и добавить 2 новых')
    matrix = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'Начальный список:\n{matrix}')
    matrix.pop(0)
    matrix.pop(0)
    matrix.append(10)
    matrix.append(11)
    print(f'Конечный список:\n{matrix}')


MY_LEN: List[List[Union[str, List[str]]]] = [
    ['БО-331101', ['Акулова Алена', 'Бабушкина Ксения']],
    ['БОВ-421102', ['Дедушкин Даниил', 'Небесный Дмитрий']],
    ['БО-331103', ['Апрошедший Александр']]
]


def task6_3() -> None:
    print('\nЗадание 6.3 - красиво вывести MY_LEN')
    for el in MY_LEN:
        print(el[0])
        for i in el[1]:
            print(f'\t{i}')


def task6_4() -> None:
    print('\nЗадание 6.4 - вывести студентов с фамилией на А')
    for el in MY_LEN:
        for i in el[1]:
            if i.startswith('А'):
                print(f'{i} ({el[0]})')


def main() -> None:
    print("""
ij  Номера функций:
    Задание 1
11. Задание 1-1
12. Задание 1-2
13. Задание 1-3
14. Задание 1-4
    Задание 2 «Строки и списки»
21. Задание 2-1
22. Задание 2-2
23. Задание 2-3
24. Задание 2-4
    Задание 3 «Матрицы»
31. Задание 3-1
32. Задание 3-2
34. Задание 3-4
35. Задание 3-5
36. Задание 3-6
37. Задание 3-7
38. Задание 3-8
    Задание 4 «Строки»
41. Задание 4-1
42. Задание 4-2
43. Задание 4-3
44. Задание 4-4
    Задание 6 «Списки»
61. Задание 6-1
62. Задание 6-2
63. Задание 6-3
64. Задание 6-4
00. Выход из программы        
        """)

    functions = [
        [task1_1, task1_2, task1_3, task1_4],
        [task2_1, task2_2, task2_3, task2_4],
        [task3_1, task3_2, None, task3_4, task3_5, task3_6, task3_7, task3_8],
        [task4_1, task4_2, task4_3, task4_4],
        None,
        [task6_1, task6_2, task6_3, task6_4],
    ]

    while True:
        ans = input('[MENU] Введите двузначный номер функции: ')
        if len(ans) == 2:
            i, j = map(int, ans)

            if i == 3:
                print('Начальная матрица:')
                pprint(MATRIX)
            elif i == 4:
                print('MY_STRING:')
                print(MY_STRING)
            elif i == 6 and j > 2:
                print('MY_LEN:')
                pprint(MY_LEN)

            functions[i - 1][j - 1]()
        elif ans == '0':
            break


if __name__ == "__main__":
    main()
