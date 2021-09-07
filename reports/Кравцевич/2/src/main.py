import math
import random

matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2]
]


def task1():
    a, b, c, d, f = int(input('Enter a: ')), int(input('Enter b: ')), int(input('Enter c: ')), int(input('Enter d: ')), \
                    int(input('Enter f: '))
    print('Result: ',
          math.fabs(1 - (a * b ** c) - a * (b ** 2 - c ** 2) + (b - c + a) * (12 + b) / (c - a)) if c - a != 0 else 0)


def task2():
    size = int(input('Enter list size: '))
    l = [input('Enter next element: ') for _ in range(size)]
    print('Result:', *l[::2], sep=' ')


def task3():
    size = int(input('Enter list size: '))
    l = [int(input('Enter next element: ')) for _ in range(size)]
    output = 1
    for num in [x for x in l if x < 10]:
        output *= num

    return output


def task4():
    size = int(input('Enter list size: '))
    l = [int(input('Enter next element: ')) for _ in range(size)]
    return sum(l) / len(l)


def task5():
    my_number = int(input('First number: '))
    user_number = int(input('Second number: '))
    while user_number == my_number:
        user_number = input()


def task6():
    size = int(input('Enter list size: '))
    l = [input('Enter next element: ') for _ in range(size)]

    print(*[x for x in l if x.endswith('r')], sep=' ')


def task7():
    numbers = [str(random.randint(0, 9)) for _ in range(6)]
    if 3 not in numbers:
        numbers[random.randint(0, 5)] = '3'

    output = ''.join(numbers)
    print(output)
    return output


def task8():
    s = input('Enter string: ')
    print('Л' * len(s))


def task9():
    for row_index, line in enumerate(matrix):
        for col_index, element in enumerate(line):
            if element < 5:
                matrix[row_index][col_index] **= 2

    return matrix


def task10():
    for line in matrix:
        print(sum([item if item % 2 == 0 else 0 for item in line]))


def task11():
    sum_less = 0
    sum_more = 0
    for line in matrix:
        sum_less += sum([item if item < 5 else 0 for item in line])
        sum_more += sum([item if item >= 5 else 0 for item in line])

    print(max(sum_less, sum_more))


def task12():
    global matrix
    matrix = matrix[:-4]
    print(*matrix, sep='\n')


def task13():
    global matrix
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
    print(*matrix, sep='\n')


def task14():
    number = int(input())
    output = 0
    for line in matrix:
        output += line.count(number)
    print(output)


def task15():
    text = input('Enter text: ')
    for chr in ',.:-;':
        text.replace(chr, '')
    output = ''
    for s in text.split(' '):
        if len(s) >= 5 and len(s) <= 10:
            output += s + ' '
    print(output.strip())


def task16():
    students = input('Enter info about students: ')
    str = '{0:10}{1:15}{2:15}{3:30}'
    splited = students.split(';')

    lastname = splited[::5]
    firstname = splited[1::5]
    fath = splited[2::5]
    age = splited[3::5]
    category = splited[4::5]
    category[0] = 'О Студенте'
    age[0] = ''

    for i in range(len(lastname)):
        print(str.format(lastname[i], firstname[i], fath[i], (category[i] + ', ' + age[i])).strip(', '))


def task17():
    students = input('Enter info about students: ')
    splited = students.split(';')

    output = '{0:30}{1:10}{2:15}'
    fullname = splited[::3]
    age = splited[1::3]
    category = splited[2::3]
    print(output.format(fullname[0], age[0], category[0]))

    for i in range(1, len(age)):
        if int(age[i].split(' ')[0]) > 21:
            print(output.format(fullname[i], age[i], category[i]))


def task18():
    s = input('Enter string')
    print('Len: ', len(s))
    print('Words count: ', len(s.split()))


def task19():
    output = []
    for line in matrix:
        output += line

    print(output)
    print(sum(output))


def task20():
    size = 10
    l = [int(input('Enter next element: ')) for _ in range(size)]

    l = l[:3] + l[8:] + [1, 2]
    print('Result: ', l)


def task21(l):
    # ['Name', ['', '', '']]
    for group in l:
        print(group[0])
        print(*group[1], sep='\n')


def task22(l):
    for group in l:
        print(group[0])
        for student in group[1]:
            splited = student.split(' ')
            if splited[0].startswith('П') and splited[-1].startswith('А'):
                print(student)


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
    choice = int(input('Ваш выбор: '))

    if choice > 0:
        options[choice]()


if __name__ == '__main__':
    menu()
