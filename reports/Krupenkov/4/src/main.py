from random import choice
import random


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
    str = input('\nЗадание 2 №3\nВедите строку: ')
    new_str = ''
    for symbol in str:
        if symbol.isdigit():
            new_str += symbol
    print(new_str)


# z1_1()
# z1_2()
# z1_3()
# z1_4()
# z2_1()
# z2_2()
# z2_3()
# z2_4()