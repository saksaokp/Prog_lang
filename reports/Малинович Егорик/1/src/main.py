# 1
def task1_1_4():
    a = float(input("Введите а: "))
    b = float(input("Введите б: "))
    c = float(input("Введите с: "))
    d = float(input("Введите д: "))
    f = float(input("Введите ф: "))
    if a != 0:
        result = float(abs(a - b * c * d ** 3 + (c ** 5 - a ** 2) / a + f ** 3 * (a - 213)))
        print(result)
    else:
        print("ошибочка")


def task1_2_4():
    a = [300, "haha", 1488, "bymbym", 228, "kaka", 1337, "yep", 1, "gg"]
    for i in range(len(a)):
        if i % 2 == 1:
            print(a[i])


def task1_3_4():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    x = 1
    for i in a:
        if i > 10:
            x = x * i
    print(x)


def task1_4_4():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    i = len(a) // 2
    print(a[i])


# 2
def task2_1_4():
    a = 7
    while True:
        x = int(input("Введите число: "))
        if x < a:
            break


def task2_2_4():
    a = ['spam', 'road', 'ham', 'red']

    for i in a:
        if i[0] == 'r':
            print(i)


def task2_3_4():
    import string
    import random

    some_str = ''
    some_seq = string.ascii_letters + string.digits

    for i in range(8):
        some_str += random.choice(some_seq)

    if some_str.isalpha():
        some_str[random.randint(0, 7)] = random.choice(string.digits)

    print(some_str)


def task2_4_4():
    orig_str = 'i wanna 2 ham and 1 spam'

    new1 = ''
    new2 = ''

    for char in orig_str:
        if char.isalpha():
            new1 += char
        if char.isdigit():
            new2 += char

    print(new1)
    print(new2)


# 3
a = [[1, 2, 3, 4, 5, 6, 7, 8],
     [8, 7, 6, 5, 4, 3, 2, 1],
     [2, 3, 4, 5, 6, 7, 8, 9],
     [9, 8, 7, 6, 5, 4, 3, 2],
     [1, 3, 5, 7, 9, 7, 5, 3],
     [3, 1, 5, 3, 2, 6, 5, 7],
     [1, 7, 5, 9, 7, 3, 1, 5],
     [2, 6, 3, 5, 1, 7, 3, 2]]


def task3_1_4(a):
    for i in range(len(a)):
        if i < 4:
            for j in a[i]:
                print(j ** 2)
    print('\n')


def task3_2_4(a):
    x = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in a:
        for j in range(len(i)):
            if i[j] % 2 == 0:
                x[j] += +i[j]
    print(x)


def task3_4_4(a):
    for i in a:
        for j in a:
            j = 0
        print(i)


def task3_5_3(a):
    for i in range(len(a)):
        if i == 5:
            print(i ** 2)


def task3_6_3(a):
    element = a.clear()
    print(element)
    print(a)


def task3_7_3(a):
    s = 0
    for row in a:
        for elem in row:
            if elem == 3:
                s += 1
    return s


# 4
def task4_1_4():
    my_string = "Пусть дана строка, состоящая из слов, пробелов и знаков препинания. На основании этой строки создайте новую (и выведите ее на консоль)"
    ov_string = list(filter(lambda x: x[-2:] == 'ов', my_string.split()))
    print(ov_string)



def task4_32_4():
    my_string = '''ФИО;Возраст;Категория;_Иванов Иван Иванович;23
    года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2
    курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав
    Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21
    год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1
    курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров
    Всеволод Борисович;21 год;Студент 2 курса'''.replace('\n', ' ')
    # первое задание
    list_data = my_string.split('_')
    cap = ' '.join(list_data[0].split(';'))
    data = [' '.join(i.split(';')) for i in list_data[1:]]
    print(cap + '\n')
    print(*data, sep='\n')
    print()
    # второе задание на основе первого
    for name in data:
        if name[0] in 'АБ':
            print(name)


def task4_4():
    s = "Какой-то текст"
    syms = len(s)  # число символов
    syms2 = len(s) - s.count(' ')  # число символов без пробелов
    words = s.count(' ') + 1  # число слов
# 6
def task6_1_2():
    a = []
    k = 10
    for r in range(6):
        a.append([])
        for c in range(6):
            a[r].append(k)
            k += 1

    for r in a:
        print(r)

def task6_2_3():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in a:
        if i % 2 == 0:
         a.remove(i)
    a.append(33)
    a.append(22)
    a.append(11)
    a.append(55)
    a.append(44)
    print(a)
def task6_3_4():
    my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения']],
              ['БОВ-421102', []], [' БО-331103', []]]

    for i in my_len:
        if int(i[0][-1]) % 2 == 0:
            print(i)

def f1():
    print("Функция 1")


def f2():
    print("Функция 2")


def f3():
    print("Функция 3")


while True:
    x = int(input())
    if x == 0:
        break
    elif x == 1:
        f1()
    elif x == 2:
        f2()
    elif x == 3:
        f3()
    else:
        print('Некорректный ввод')

    y = input('Вы хотите продолжить?')
    if y == "0" or y == 'no' or y == 'N' or y == 'нет': break
    if y == "1" or y == 'yes' or y == 'Y' or y == 'да': continue

