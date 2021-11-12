from statistics import mean
import re
from random import choice
from string import digits
from random import randint
#Задание 1
def task_1_1():
    print("Введите данные:\n")
    a = int (input("a:"))
    b = int(input("b:"))
    c = int (input("c:"))
    d = abs(1 - a*(b**c) - a*((b**2)-(c**2)) + (b - c + a)*(12+b)/(c*a))
    print("Резултат: ", d)

def task_1_2():
    list = [22, "чётный", 12.5, 78, 42]
    for i in list:
        if (list.index(i)) % 2 == 0 : print("Чётные элементы в списке:", i)

def task_1_3():
    list = [12, 8, 33, 2, 5, 66]
    list1 = []
    a = 1
    for i in list:
        if i < 10: a *= i
    print (a)

def task_1_4():
    list = [5, 7, -15, 12.6, 24.4]
    print("Числа в списке:", list)
    list_avg = mean(list)
    print("Cреднее арифметическое: ", list_avg)

#Задание 2
def task_2_1():
    my_number = 8
    user_number = int (input("Введите число: "))
    while user_number == my_number: user_number = int (input("Введите число: "))

def task_2_2():
    list = ["suptember", "egg", "sun", "monster"]
    for i in list:
        if i[-1] == "r": print(i)
def task_2_3():
    while True:
        res = [randint(0, 6)  for _ in range(6)]
        if 3 in res: break
    print(''.join(map(str,res)))

def task_2_4():
    string = "Строка"
    l = "Л"
    string = l*len(string)
    print(string)

    #Задание 3
def task_3_1(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i][j] < 5: list[i][j]= list[i][j]**2
    for i in range(len(list)):
        for j in range(len(list)): 
            print(list[i][j], end=" ")
        print("\n")

def task_3_2(list):
       for i in range(len(list)):
           a = 0
           for j in range(len(list)): 
            if list[i][j] % 2 == 0:
                a+=list[i][j]
           print(a, "\n")

def task_3_4(list):
           a = b = 0
           for i in range(len(list)):
                for j in range(len(list)): 
                    if list[i][j] < 5: a += list[i][j]
                    else: b += list[i][j]
           print("Сумма чисел меньше 5 равна: ", a)
           print("Сумма остальных чисел равна: ", b)
           print("Большее число: ")
           if a > b: print(a)
           else: print(b)

def task_3_5(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i][j] % 2 == 0: list[i][j] = 0
    print(*list, sep = '\n')

def task_3_6(list):
    a = int(input("Введите номер строки, которую вы хотите удалить:"))
    del list[a - 1]
    print(*list, sep = '\n')
def task_3_7(list):
    print("Мартрица до изменения:")
    print(*list, sep = '\n')
    help1 = list[0]
    help2 = list[len(list) - 1]
    list[0] =  help2
    list[len(list) - 1] = help1
    print("Мартрица после изменения:")
    print(*list, sep = '\n')

    #Задание 4
def task_4_1():
    string = "Стремитесь не к успеху, а к ценностям, которые он дает."
    l = string.split(' ')
    string = ""
    for i in l :
        if 4 < len(i) < 11: string = string + i + " "
    print (string)

def task_4_2():
    my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семён;Игоревич;22 года;Студент 2 курса;"
    my_string = my_string.replace(";", "\t")
    my_string = my_string.replace("Категория", "О студенте")
    my_string = my_string.replace("Возраст", "")
    my_string = my_string.replace("_", "\n")

    print (my_string)

def task_4_3():
    my_string = """Ф;И;О;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семён Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович; 21 год; Студент 1 курса;_Петров Семен Семенович; 21 год; Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович; 21 год; Студент 2 курса"""
    ls = my_string.split(';_')
 
    for i in ls[1:]:
        fio, age, cat = i.split(';')
        a, b = age.split()
        if int(a) > 21:
            print(fio, age, cat)
   
def task_4_4():
    s = "Тут что-то должно быть написано"
    syms = len(s)
    syms2 = len(s) - s.count(' ')
    words = s.count(' ') + 1
    print('Количество символов: ', syms2)
    print('Количество слов: ', words)

    #Задание 6
def task_6_1():
    a = []
    k = 10  
    for r in range(6):  
        a.append([])  
        for c in range(6):  
            a[r].append(k)  
            k += 1   
    print(sum(sum([i for i in x])for x in a))

def task_6_2():
    spisok =[8, 5, 9, 3, 5, 0, 7, 4, 2, 10]
    print(spisok)
    print("Список после изменений:")
    del spisok[4:8]
    spisok.append(11)
    spisok.append(12)
    print(spisok)

def task_6_3():
    my_len = [["БО-331101",["Акулова Алёна", "Бабушкина Ксения", "Попов Алексей"]], ["БОВ-421102",["Нагиев Дмитрий", "Колбаскин Артём", "Душнов Иван" ]],["БО-331103",["Помидоркин Артур", "Капустина Кристина", "Картошкина Алиса"]]]
    for i in my_len:
        grup = i
        print (grup[0])
        fio = grup[1]
        for k in range(len(fio)):
            print(fio[k])
            
def task_6_4():
    my_len = [["БО-331101",["Акулова Алёна", "Бабушкина Ксения", "Попов Алексей"]], ["БОВ-421102",["Нагиев Дмитрий", "Колбаскин Артём", "Душнов Иван" ]],["БО-331103",["Помидоркин Артур", "Капустина Кристина", "Картошкина Алиса"]]]
    for i in my_len:
        grup = i
        fio = grup[1]
        a = group[0]
        for k in fio:
            fam, name = k.split(" ")
            if fam[0] == "П" and name[0] == "А":
                print(fam, name, a)

def task_1():
            while True:
                cmd = input("Введите номер пункта задания:")
                if int(cmd) == 1:
                    task_1_1()
                elif int(cmd) == 2:
                    task_1_2()
                elif int(cmd) == 3:
                    task_1_3()
                elif int(cmd) == 4:
                    task_1_4()
                else: print("Ошибка ввода")
                ch =  input("Продолжить? Y - 1, N - 0: ")
                if int(ch) == 0: break
                else: print("Ошибка ввода")

def task_2():
            while True:
                cmd = input("Введите номер пункта задания:")
                if int(cmd) == 1:
                    task_2_1()
                elif int(cmd) == 2:
                    task_2_2()
                elif int(cmd) == 3:
                    task_2_3()
                elif int(cmd) == 4:
                    task_2_4()
                else: print("Ошибка ввода")
                ch =  input("Продолжить? Y - 1, N - 0: ")
                if int(ch) == 0: break
                else: print("Ошибка ввода")

def task_3(list):
            while True:
                cmd = input("Введите номер пункта задания(условия для третьего задания нету :3 ):")
                if int(cmd) == 1:
                    task_3_1(list)
                elif int(cmd) == 2:
                    task_3_2(list)
                elif int(cmd) == 4:
                    task_3_4(list)
                elif int(cmd) == 5:
                    task_3_5(list)
                elif int(cmd) == 6:
                    task_3_6(list)
                elif int(cmd) == 7:
                    task_3_7(list)
                else: print("Ошибка ввода")
                ch =  input("Продолжить? Y - 1, N - 0: ")
                if int(ch) == 0: break
                else: print("Ошибка ввода")

def task_4():
            while True:
                cmd = input("Введите номер пункта задания:")
                if int(cmd) == 1:
                    task_4_1()
                elif int(cmd) == 2:
                    task_4_2()
                elif int(cmd) == 3:
                    task_4_3()
                elif int(cmd) == 4:
                    task_4_4()
                else: print("Ошибка ввода")
                ch =  input("Продолжить? Y - 1, N - 0: ")
                if int(ch) == 0: break
                else: print("Ошибка ввода")

def task_6():
            while True:
                cmd = input("Введите номер пункта задания:")
                if int(cmd) == 1:
                    task_6_1()
                elif int(cmd) == 2:
                    task_6_2()
                elif int(cmd) == 3:
                    task_6_3()
                elif int(cmd) == 4:
                    task_6_4()
                else: print("Ошибка ввода")
                ch =  input("Продолжить? Y - 1, N - 0: ")
                if int(ch) == 0: break
                else: print("Ошибка ввода")

def main():
    list = [[1, 2, 3, 4, 5, 6, 7, 8],
           [8, 7, 6, 5, 4, 3, 2, 1],
           [2, 3, 4, 5, 6, 7, 8, 9],
           [9, 8, 7, 6, 5, 4, 3, 2],
           [1, 3, 5, 7, 9, 7, 5, 3],
           [3, 1, 5, 3, 2, 6, 5, 7],
           [1, 7, 5, 9, 7, 3, 1, 5],
           [2, 6, 3, 5, 1, 7, 3, 2]]
    while True:
        print("Вариант 11")
        print("1 - Задание 1")
        print("2 - Задание 2")
        print("3 - Задание 3")
        print("4 - Задание 4")
        print("6 - Задание 6")
        print("0 - Выход")
        cmd_m = input("Введите команду:")
        if int(cmd_m) == 0: break
        elif int(cmd_m) == 1: task_1()
        elif int(cmd_m) == 2: task_2()
        elif int(cmd_m) == 3: task_3(list)
        elif int(cmd_m) == 4: task_4()
        elif int(cmd_m) == 5: task_6()
        else: print("Ошибка ввода")

main()