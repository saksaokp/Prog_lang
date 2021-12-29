import numpy as np
import re
import random
import time
import os
###################################
def z1_1():
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    c = int(input('Введите c: '))
    d = int(input('Введите d: '))
    k = int(input('Введите k: '))
    if b==0 or a==0:
        print('(!) Неправильный ввод ("b" или "a" не могут быть равны нулю)')
    else:
        sum = abs((((a**2) - (b**3) - (c**3 * a**2))*(b-c+(c*(k-d/b**3))) - (k/b - k/a)*c)**2 - 20000)
    print('Ответ: ')
    print(sum)
###################################
def z1_2():
    print('Введите произвольный список с числами: ')
    A = list(map(int, input().split()))
    print('Все нечетные элементы: ')
    for i in A:
        if(i%2)==1:
            print(i)
###################################            
def z1_3():
    print('Введите произвольный список, содержащий только числа: ')
    A = list(map(int, input().split()))
    print('Сумма всех чисел 0<X<10: ')
    sum = 0
    for i in A:
        if i>=1 and i<=10:
            sum = sum + i
    print(sum)
###################################    
def z1_4():
    print('Введите произвольный список с числами: ')
    A = list(map(int, input().split()))
    print('Минимальное число: ')
    print(min(A))
###################################    
def z2_1():
    print('Вводите число user_number пока оно не будет равно 25: ')
    my_number = 25
    user_number = int(input())
    while my_number!=user_number:
        user_number = int(input())
###################################        
def z2_2():
    print('Введите список со строками: ')
    A = list(map(str, input().split()))
    print('Все строки меньше 10 символов: ')
    for i in A:
        if len(i)<10:
            print(i)
###################################            
def z2_3():
    N = int(input('Введите N:'))
    S = ''
    while N!=0:
        N = N - 1
        S = S + 'R'
    print(S)
###################################
def z2_4():
    text = str(input('Введите строку:'))
    text = re.sub("0", "", text)
    text = re.sub("1", "", text)
    text = re.sub("2", "", text)
    text = re.sub("3", "", text)
    text = re.sub("4", "", text)
    text = re.sub("5", "", text)
    text = re.sub("6", "", text)
    text = re.sub("7", "", text)
    text = re.sub("8", "", text)
    text = re.sub("9", "", text)
    print('Та же строка, но без цифр: ')
    print(text)
###################################
def z3_1():
    print('Возведение всех четных эл-тов в квадрат')
    A = np.array([[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1],[2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2],[1,3,5,7,9,7,5,3],[3,1,5,3,2,6,5,7],[1,7,5,9,7,3,1,5],[2,6,3,5,1,7,3,2]])
    for i in A:
        print(i)
    for i in A:
        for j in i:
            if (j%2)==0:
                j=j*2
    print('Результат: ')
    print(A)
###################################
def z3_2():
    print('Сложение эл-тов матрицы по столбцам: ')
    A = np.array([[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1],[2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2],[1,3,5,7,9,7,5,3],[3,1,5,3,2,6,5,7],[1,7,5,9,7,3,1,5],[2,6,3,5,1,7,3,2]])
    sum1=sum2=sum3=sum4=sum5=sum6=sum7=sum8=0
    for i in A:
        print(i)
        count=0 
        for j in i:
            count=count+1
            if count==1:sum1=sum1+j
            if count==2:sum2=sum2+j
            if count==3:sum3=sum3+j
            if count==4:sum4=sum4+j
            if count==5:sum5=sum5+j
            if count==6:sum6=sum6+j
            if count==7:sum7=sum7+j
            if count==8:sum8=sum8+j
    print("Первый столбик: ", sum1)
    print("Второй столбик: ", sum2)
    print("Третий столбик: ", sum3)
    print("Четвертый столбик: ", sum4)
    print("Пятый столбик: ", sum5)
    print("Шестой столбик: ", sum6)
    print("Седьмой столбик: ", sum7)
    print("Восьмой столбик: ", sum8)
###################################
def z3_4():
    print('Сложение всех эл-тов матрицы')
    A = np.array([[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1],[2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2],[1,3,5,7,9,7,5,3],[3,1,5,3,2,6,5,7],[1,7,5,9,7,3,1,5],[2,6,3,5,1,7,3,2]])
    for i in A:
        print(i)
    sum=0
    for i in A:
        for j in i:
            sum+=j
    print('Результат: ')
    print(sum)
###################################    
def z3_5():
    print('Замена чисел на введённое: ')
    A = np.array([[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1],[2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2],[1,3,5,7,9,7,5,3],[3,1,5,3,2,6,5,7],[1,7,5,9,7,3,1,5],[2,6,3,5,1,7,3,2]])
    for i in A:
        print(i)
    replace=int(input('Введите число для замены: '))
    for i in range(8):
        for j in range(8):
            if A[i][j]<replace:
                A[i][j]=replace
    print(A)
###################################    
def z3_6():
    print('Удаление столба матрицы: ')
    A = [[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1],[2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2],[1,3,5,7,9,7,5,3],[3,1,5,3,2,6,5,7],[1,7,5,9,7,3,1,5],[2,6,3,5,1,7,3,2]]
    for i in A:
        print(i)
    delete=int(input('Введите номер столба для удаления: '))
    delete=delete-1
    for i in A:
        i.pop(delete)
    for i in A:
        print(i)
###################################        
def z3_7():
    print('Заполнение нулями матрицы NxM: ')
    N = int(input('Введите кол-во строк: '))
    M = int(input('Введите кол-во столбов: '))
    A = [[0 for y in range(M)] for x in range(N)]
    for i in A:
        print(i)
###################################        
def z3_8():
    print('Возведение строки матрицы в квадрат')
    A = np.array([[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1],[2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2],[1,3,5,7,9,7,5,3],[3,1,5,3,2,6,5,7],[1,7,5,9,7,3,1,5],[2,6,3,5,1,7,3,2]])
    for i in A:
        print(i)
    delete=int(input('Введите номер строки для возведения в квадрат: '))
    delete=delete-1
    for j in range(8):
        A[delete][j-1] = A[delete][j-1]**2
    print(A[delete])
###################################    
def z4_1():
    print('Вывод слов, начинающихся на "ли":')
    text=input('Введите строку: ')
    filtered=''
    for i in text.split():
        if i.startswith('Ли') or i.startswith('ли'):
            filtered=filtered+i+' '
    print('Обработанная строка: ', filtered)
###################################
def z4_2():
    print('Вывод информации в виде таблицы: ')
    my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'
    my_string_w=my_string.replace("_", "")
    rows=int((len(my_string_w.split(';'))-5)/5)
    print(rows)
    print(my_string.split(';')[0], my_string.split(';')[1], my_string.split(';')[2], sep='', end=' ', flush=True)
    print(my_string.split(';')[3], my_string.split(';')[4], sep=' ', flush=True)
    for i in range(rows):
        for j in range(5):
            if j==0:
                print(my_string_w.split(';')[i*5 + 5 + j], end=' ', flush=True)
            if j==1:
                print(my_string_w.split(';')[i*5 + 5 + j], end=' ', flush=True)
            if j==2:
                print(my_string_w.split(';')[i*5 + 5 + j], end=' ', flush=True)
                x=len(my_string_w.split(';')[i*5 + 5 + j])+len(my_string_w.split(';')[i*5 + 4 + j])+len(my_string_w.split(';')[i*5 + 3 + j]) + 3
                l=30-x
                for b in range(l):
                    print(' ', sep='', end='', flush=True)
            if j==3:
                print(my_string_w.split(';')[i*5 + 5 + j], end=' ', flush=True)
                x=len(my_string_w.split(';')[i*5 + 5 + j])
                l=15-x
                for b in range(l):
                    print(' ', sep='', end='', flush=True)
            if j==4:
                print(my_string_w.split(';')[i*5 + 5 + j], end=' ', flush=True)
        print('')
###################################        
def z4_3():
    print('Вывод информации в таблицу, где возраст всех студентов 21 год: ')
    my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса;_Иванов;Семен;Игоревич;22 года;Студент 2 курса;_Акибов;Ярослав;Наумович;23 года;Студент 3 курса;_Борков;Станислав;Максимович;21 год;Студент 1 курса;_Петров;Семен;Семенович;21 год;Студент 1 курса;_Романов;Станислав;Андреевич;23 года;Студент 3 курса;_Петров;Всеволод;Борисович;21 год;Студент 2 курса'
    my_string_w=my_string.replace("_", "")
    rows=int((len(my_string_w.split(';'))-5)/5)
    print(my_string.split(';')[0], my_string.split(';')[1], my_string.split(';')[2], sep='', end=' ', flush=True)
    print(my_string.split(';')[3], my_string.split(';')[4], sep=' ', flush=True)
    for i in range(rows):
        for j in range(5):
            if my_string_w.split(';')[i*5 + 5 + 3]=='21 год':
                if j==0:
                    print(my_string_w.split(';')[i*5 + 5 + j], end=' ', flush=True)
                if j==1:
                    print(my_string_w.split(';')[i*5 + 5 + j], end=' ', flush=True)
                if j==2:
                    print(my_string_w.split(';')[i*5 + 5 + j], end=' ', flush=True)
                    x=len(my_string_w.split(';')[i*5 + 5 + j])+len(my_string_w.split(';')[i*5 + 4 + j])+len(my_string_w.split(';')[i*5 + 3 + j]) + 3
                    l=30-x
                    for b in range(l):
                        print(' ', sep='', end='', flush=True)
                if j==3:
                    print(my_string_w.split(';')[i*5 + 5 + j], end=' ', flush=True)
                    x=len(my_string_w.split(';')[i*5 + 5 + j])
                    l=15-x
                    for b in range(l):
                        print(' ', sep='', end='', flush=True)
                if j==4:
                    print(my_string_w.split(';')[i*5 + 5 + j], end=' ', flush=True)
        print('')
###################################        
def z4_4():
    my_string = input('Введите строку: ')
    slov=len(my_string.split(' '))
    simv=len(my_string)
    print('Слов: ', slov)
    print('Символов: ', simv)
###################################    
def z6_1():
    summa=0
    N = int(input('Введите кол-во строк и столбцов матрицы: '))
    A = [[int(random.uniform(10, 30)) for y in range(N)] for x in range(N)]#заполнение случайными числами от 10 до 30
    for i in A:
        print(i)
    for i in A:
        for b in i:
            summa=summa+b
    print('')
    print('сумма всех эл-тов: ', summa)
###################################    
def z6_2():
    print('Удаление четных эл-тов списка и добавление 2 новых: ')
    spis=list(map(int, input('Введите список чисел: ').split()))
    a=0
    while a<len(spis):
        if spis[a]%2==0:
            spis.pop(a)
        a=a+1
    spis.append(15)
    spis.append(20)
    print('Список: ')
    print(spis)
###################################    
def z6_3():
    print('Вывод информации в виде <Название группы>: <ФИО>; <ФИО>...:')
    my_len = [['БО-3',['Акулова Алёна', 'Бабушкина Ксения']], ['БОВ-4',['Селёдкин Андрей', 'Курылов Максим']], ['БО-331',['Силин Сергей','Широкий Павел']]]
    for i in range(len(my_len)):
        print(my_len[i][0], end=': ')
        for j in my_len[i][1]:
            print(j, end='; ')
        print('')
###################################        
def z6_4():
    print('Вывод информации в виде <Название группы>: <ФИО>; <ФИО>... (но только где фамилия студента меньше 7 букв):')
    my_len = [['БО-3',['Акулова Алёна', 'Бабушкина Ксения', 'Пищ Алексей']], ['БОВ-4',['Селёдкин Андрей', 'Курт Кирилл', 'Курылов Максим']], ['БО-331',['Силин Сергей','Широкий Павел']]]                                           
    print('')
    for i in range(len(my_len)):
        print(my_len[i][0], end=': ')
        for j in range(len(my_len[i][1])):
            if len(my_len[i][1][j].split(' ')[0])<7:
                print(my_len[i][1][j], end='; ')
        print('')
###################################        
def menu():
    a=1
    while a==1:
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        print('Выберите пункт меню: ')
        print('0 - Выход из программы ')
        print('1 - Задание 1')
        print('2 - Задание 2')
        print('3 - Задание 3')
        print('4 - Задание 4')
        print('6 - Задание 6')
        zadanie=int(input('выбор: '))
        clearConsole()
        if zadanie==0:break
        if zadanie==1:
            print('0 - Вернуться назад ')
            print('1 - Задание 1.1 ')
            print('2 - Задание 1.2 ')
            print('3 - Задание 1.3 ')
            print('4 - Задание 1.4 ')
            act=int(input('выбор: '))
            clearConsole()
            if act==1:z1_1()
            if act==2:z1_2()
            if act==3:z1_3()
            if act==4:z1_4()
            if act==0:print('')
        if zadanie==2:
            print('0 - Вернуться назад ')
            print('1 - Задание 2.1 ')
            print('2 - Задание 2.2 ')
            print('3 - Задание 2.3 ')
            print('4 - Задание 2.4 ')
            act=int(input('выбор: '))
            clearConsole()
            if act==1:z2_1()
            if act==2:z2_2()
            if act==3:z2_3()
            if act==4:z2_4()
            if act==0:print('')
        if zadanie==3:
            print('0 - Вернуться назад ')
            print('1 - Задание 3.1 ')
            print('2 - Задание 3.2 ')
            print('3 - Задание 3.3 ')
            print('4 - Задание 3.4 ')
            print('5 - Задание 3.5 ')
            print('6 - Задание 3.6 ')
            print('7 - Задание 3.7 ')
            print('8 - Задание 3.8 ')
            act=int(input('выбор: '))
            clearConsole()
            if act==1:z3_1()
            if act==2:z3_2()
            if act==3:z3_3()
            if act==4:z3_4()
            if act==5:z3_5()
            if act==6:z3_6()
            if act==7:z3_7()
            if act==8:z3_8()
            if act==0:print('')
        if zadanie==4:
            print('0 - Вернуться назад ')
            print('1 - Задание 4.1 ')
            print('2 - Задание 4.2 ')
            print('3 - Задание 4.3 ')
            print('4 - Задание 4.4 ')
            act=int(input('выбор: '))
            clearConsole()
            if act==1:z4_1()
            if act==2:z4_2()
            if act==3:z4_3()
            if act==4:z4_4()
            if act==0:print('')
        if zadanie==6:
            print('0 - Вернуться назад ')
            print('1 - Задание 6.1 ')
            print('2 - Задание 6.2 ')
            print('3 - Задание 6.3 ')
            print('4 - Задание 6.4 ')
            act=int(input('выбор: '))
            clearConsole()
            if act==1:z6_1()
            if act==2:z6_2()
            if act==3:z6_3()
            if act==4:z6_4()
            if act==0:print('')
        if act!=0: 
            cont=input('Хотите продолжить? Y-Да, N-Нет: ')
            if cont=='N' or cont=='n': break
    print('Выход...')
    time.sleep(2)
###################################        

menu()

