from math import fabs as mod
from random import randrange as rand


def formula(a, b, c, k):
    return mod((a ** 2 / b ** 2 + c ** 2 * a ** 2) / (a + b + c * (k - a / b ** 3)) + c + (k / b - k / a) * c)


def T1():
    var = []
    for i in range(4):
        var.append(int(input()))
    print(formula(var[0], var[1], var[2], var[3]))


def T2():
    lst = []
    for i in range(20):
        lst.append(rand(0, 100, 1))
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            print(lst[i])


def T3():
    lst = []
    sum = 0
    for i in range(10):
        lst.append(rand(0, 15, 1))
    for i in range(len(lst)):
        if lst[i] / 10 >= 1:
            sum = sum + lst[i]
    print(sum)


def T4():
    lst = []
    max = 0
    for i in range(10):
        lst.append(rand(0, 15, 1))
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    print(max)


def T5():
    from random import randrange as rand
    my_number = rand(0, 10)
    user_number = 10
    while user_number >= my_number:
        user_number = int(input())
    print("You win!")


def T6():
    lst = []
    max = 0
    for i in range(10):
        lst.append(str(rand(10000, 9999999999, 1)))
    for i in range(len(lst)):
        print(lst[i])


def T7():
    string = ""
    for i in range(5):
        string = string + chr(rand(1040, 1072))
    print(string)


def T8():
    string = "Я каменщик, работаю 3 дня"
    nstr = ""
    for i in range(len(string)):
        if (ord(string[i]) >= 48) and (ord(string[i]) <= 57):
            nstr = nstr + string[i]
    print(nstr)


matr = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2]
]


def T9():
    for i in range(8):
        for k in range(8):
            matr[i][k] = matr[i][k] ** 2
    for i in range(8):
        for k in range(8):
            print(matr[i][k], end="\t")
        print()


def T10():
    sum = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        for k in range(8):
            sum[i] = sum[i] + matr[i][k]
    print(sum)


def T11():
    sum = [1, 8, 2, 9, 1, 3, 1, 2]
    for i in range(8):
        for k in range(1, 8):
            sum[i] = sum[i] * matr[i][k]
    print(sum)


def T12():
    for i in range(8):
        for k in range(8):
            matr[i][k] = matr[i][k] * (matr[i][k] % 2)
    print(matr)


def T13():
    matrtemp = matr
    delete = int(input())
    matrtemp.pop(delete)
    print(matrtemp)


def T14():
    matrtemp = matr
    chng = []
    for i in range(8):
        chng.append(matrtemp[0][i])
    matrtemp[0] = matrtemp[7]
    matrtemp[7] = chng
    print(matrtemp)


def T15():
    string = "!,!Ihate am !stonecutter? i -am working. forlk a 3 dayskiuiu!?.,"
    stringres = ""
    bl = "nobreak"
    i = 0
    words = string.split()
    while i != len(words) - 1:
        for i in range(len(words)):
            bl = "nobreak"
            for k in range(len(words[i])):
                if words[i][k] == "!" or words[i][k] == "?" or words[i][k] == "." or words[i][k] == "," or words[i][
                    k] == ":" or words[i][k] == ";":
                    words[i] = words[i][:k] + words[i][k + 1:]
                    i -= 1
                    bl = "break"
                    break
            if bl == "break":
                break
    for i in range(len(words)):
        if len(words[i]) >= 5:
            stringres += words[i]
            stringres += " "
    print(string)
    print(stringres)


def T16():
    string = "Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
    Students = string.split("_")
    Info = []
    for i in range(len(Students)):
        Info.append([0, ])
    for i in range(len(Students)):
        Info[i] = Students[i].split(";")
    print("ФИО\t\t\t\t\t\t Категория\t\t\t Возраст")
    for i in range(len(Students)):
        print(Info[i][0], Info[i][1], Info[i][2], "\t", Info[i][4], "\t", Info[i][3])


def T17():
    string = "Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
    Students = string.split("_")
    Info = []
    for i in range(len(Students)):
        Info.append([0, ])
    for i in range(len(Students)):
        Info[i] = Students[i].split(";")
    print("ФИО\t\t\t\t\t\t Категория\t\t\t Возраст")
    for i in range(len(Students)):
        if Info[i][0] == "Петров":
            print(Info[i][0], Info[i][1], Info[i][2], "\t", Info[i][4], "\t", Info[i][3])


def T18():
    string = "!,!Ihate am !stonecutter? i -am working. forlk a 3 dayskiuiu!?.,"
    symbolcount = 0
    words = string.split()
    for symbol in string:
        if symbol != " ":
            symbolcount += 1
    wordscount = len(words)
    print(string)
    print("Слов:", wordscount)
    print("Символов", symbolcount)


def T19():
    from random import randrange as rand
    n = int(input())
    matr = []
    sumstr = []
    summ = 0
    for i in range(n):
        matr.append([rand(0, 100), ])
    for i in range(n):
        for k in range(n):
            matr[i].append(rand(0, 100))
    for i in range(n):
        print(matr[i])
    for i in range(n):
        for k in range(n):
            summ += matr[i][k]
        sumstr.append(summ)
        summ = 0
    for i in range(n):
        summ += sumstr[i]
    print("Сумма всех элементов: ", summ)


def T20():
    from random import randrange as rand
    matr = []
    for i in range(10):
        matr.append(rand(0, 100))
    print(matr)
    for i in range(2):
        matr.pop(0)
    for i in range(2):
        matr.append(rand(0, 100))
    print(matr)


def T21():
    string = [['БО-331101', ['Акулова Алёна', 'Бабушкина Ксения']],
              ['БОВ-421102', ['Максимина Таня', 'Хорохоров Даниил']]]
    for Group in string:
        print(Group[0])
        for Student in Group[1]:
            print(Student)


def T22():
    string = [['БО-331101', ['Акулова Алёна', 'Бабушкина Ксения']],
              ['БОВ-421102', ['Максимина Таня', 'Хорохоров Даниил']]]
    for Group in string:
        for Student in Group[1]:
            if Student[0] == 'А':
                print(Group[0])
                for Students in Group[1]:
                    print(Students)


# def TaskChoose(Task):
#     return [True]
Task = 23
while True:
    print("Выберите номер задания от 1 до 22")
    Task = int(input())
    if Task == 0:
        break
    Tasks = {
        1: T1,
        2: T2,
        3: T3,
        4: T4,
        5: T5,
        6: T6,
        7: T7,
        8: T8,
        9: T9,
        10: T10,
        11: T11,
        12: T12,
        13: T13,
        14: T14,
        15: T15,
        16: T16,
        17: T17,
        18: T18,
        19: T19,
        20: T20,
        21: T21,
        22: T22
    }
    Tasks[Task]()
    print("Желаете продолжить?")
    Agried = input()
    if (Agried != '1') and (Agried != 'Yes') and (Agried != 'Y') and (Agried != 'Да'):
        break
