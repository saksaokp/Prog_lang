def task_1():
    def task1_1():
        print('Задание 1.1:')
        print('Введите значение а: ')
        a = int(input())
        print('Введите значение b: ')
        b = int(input())
        print('Введите значение c: ')
        c = int(input())
        print('Введите значение k: ')
        k = int(input())
        if a==0 or b==0:
         print("error")
        else:
            S = abs((a**2/b**2+c**2*a**2)/(a+b+c*(k-a/b**3))+c+(k/b-k/a)*c)
            print("S=",S)

    def task1_2():
        print('Задание 1.2:')
        print('Введите список: ')
        A = list(map(int, input().split()))
        for i in A:
            if i%2==0:
                print("Чётный элемент=",i)


    def task1_3():
        print('Задание 1.3:')
        print('Введите список: ')
        A = list(map(int, input().split()))
        sum = 0
        for i in A:
            if i>10:
                sum=sum+i

        print("Сумма равна",sum)

    def task1_4():
        print('Задание 1.4:')
        A = list(map(int, input().split()))
        print("Максимальный элемент равен",max(A))
    task1_1()
    task1_2()
    task1_3()
    task1_4()


def task_2():
    def task2_1():
        print('Задание 2.1')
        my_number = 10
        print('Наше число = ', my_number)
        print('Введите число:')
        while True:
            user_number = int(input())
            if user_number >= my_number:
                break


    def task2_2():
        print('Введите список: ')
        A = list(map(str, input().split()))
        for i in A:
            if len(i)>=5 and len(i)<=10:
                print(i)



    def task2_3():

        from random import choice
        import string
        my_string = "".join(choice(string.ascii_uppercase) for i in range(5))
        print(my_string)


    def task2_4():
        S1 = "I56 lo93v34e 67yo09u 986rgd"
        S2 = ""
        for letter in S1:
            if letter.isdigit():
                S2+=letter
        print(S2)
    task2_1()
    task2_2()
    task2_3()
    task2_4()


def task_3():
    def task3_1():
        print("Задание 3.1")
        import pprint
        array = [[1, 2, 3, 4, 5, 6, 7, 8],
                [8, 7, 6, 5, 4, 3, 2, 1],
                [2, 3, 4, 5, 6, 7, 8, 9],
                [9, 8, 7, 6, 5, 4, 3, 2],
                [1, 3, 5, 7, 9, 7, 5, 3],
                [3, 1, 5, 3, 2, 6, 5, 7],
                [1, 7, 5, 9, 7, 3, 1, 5],
                [2, 6, 3, 5, 1, 7, 3, 2]]
        for i in range(8):
            for j in range(8):
                array[i][j] = array[i][j]**2
        pprint.pprint(array)


    def task3_2():
        print("Задание 3.2")
        array = [[1, 2, 3, 4, 5, 6, 7, 8],
                [8, 7, 6, 5, 4, 3, 2, 1],
                [2, 3, 4, 5, 6, 7, 8, 9],
                [9, 8, 7, 6, 5, 4, 3, 2],
                [1, 3, 5, 7, 9, 7, 5, 3],
                [3, 1, 5, 3, 2, 6, 5, 7],
                [1, 7, 5, 9, 7, 3, 1, 5],
                [2, 6, 3, 5, 1, 7, 3, 2]]
        for i in range(8):
                sum = 0
        for j in range(8):
            sum+=array[i][j]
            print(sum)



    def task3_3():
        print("Задание 3.3")
        array = [[1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2]]


        for i in range(8):
            com = 1
            for j in range(8):
                com*=array[i][j]
            print(com)




    def task3_4():
        print("Задание 3.4")
        import pprint
        print('Введите число: ')
        a = int(input())
        array = [[1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2]]
        array2 = array.pop(a-1)
        pprint.pprint(array)

    def task3_5():
        print("Задание 3.5")
        array = [[1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2]]
        for i in range(8):
            for j in range(8):
                if array[i][j] == 5:
                    array[i][j] = array[i][j] ** 2
                print(array[i][j], end = " ")
        print()


    def task3_6():
        print("Задание 3.6")
        import pprint
        array = [[1, 2, 3, 4, 5, 6, 7, 8],
                [8, 7, 6, 5, 4, 3, 2, 1],
                [2, 3, 4, 5, 6, 7, 8, 9],
                [9, 8, 7, 6, 5, 4, 3, 2],
                [1, 3, 5, 7, 9, 7, 5, 3],
                [3, 1, 5, 3, 2, 6, 5, 7],
                [1, 7, 5, 9, 7, 3, 1, 5],
                [2, 6, 3, 5, 1, 7, 3, 2]]
    def clear(array):
        for i in range(8):
            for j in range(8):
                array.clear()
        return array


    def task3_7():
        print("Задание 3.7")
        array = [[1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2]]
        counter = 0
        for i in range(8):
            for j in range(8):
                if array[i][j]==3:
                    counter+=1
        print(counter)



    def task3_8():
        print("Задание 3.8")
        import pprint
        array = [[1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2]]
        print("Введите номер строки: ")
        i = int(input())
        print("Введите номер столбца: ")
        j = int(input())
        print("Число на данной позиции: ", array[i-1][j-1])
    task3_1()
    task3_2()
    task3_3()
    task3_4()
    task3_5()
    task3_6()
    task3_7()
    task3_8()


def task_4():
    print("Задание 4.1")
    def task4_1():
        my_string = 'i love programming so much'
        res_string = ''
        _list = my_string.split()
        for i in _list:
            if len(i)>5:
                res_string+=i+' '
        print(res_string)


    def task4_2():
        print("Задание 4.2")
        my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;" \
                "_Петров;Семён;Игоревич;22 года;студент 2 курса."
        my_list = [str.split(';') for i, str in enumerate(my_string.split('_')) if i>0]
        print('{:<23}{:<10}{}'.format('ФИО', 'Возраст', 'Категория'))
        for element in my_list:
                print(element[0], element[1], element[2],' ', element[3],' ', element[4])


    def task4_3():
        print("Задание 4.3")
        my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;" \
                "_Петров;Семён;Игоревич;22 года;Студент 2 курса;" \
                "_Иванов;Семён;Игоревич;22 года;Студент 2 курса;" \
                "_Акибов;Ярослав;Наумович;23 года;Студент 3 курса;" \
                "_Борков;Станислав;Васильевич;21 год;Студент 1 курса;"\
                "_Петров;Семён;Семёнович;21 год;Студент 1 курса;"\
                "_Романов;Станислав;Андреевич;23 года;Студент 3 курса;"\
                "_Петров;Всеволод;Борисович;21 год;Студент 2 курса"
        my_list = [str.split(';') for i, str in enumerate(my_string.split('_')) if i>0]
        print('{:<33}{:<11}{}'.format('ФИО', 'Возраст', 'Категория'))
        for element in my_list:
            if element[0]=='Петров':
                print(element)


    def task4_4():
        print("Задание 4.4")
        my_string = "Banana, apple, pear, pineapple, watermelon"
        sym = len(my_string)
        sym2 = len(my_string)-my_string.count(' ')
        words = my_string.count(' ')+1
        print("Количество символов",sym2)
        print("Количество слов",words)
    task4_1()
    task4_2()
    task4_3()
    task4_4()


def task_5():
    def task5_1():
        print("Задание 5.1")
        matrix = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
        x = 0
        for i in matrix:
            for j in i:
                x += j
        print("Сумма элементов матрицы", x)


    def task5_2():
        print("Задание 5.2")
        A = [1,2,3,4,5,6,7,8,9,10]
        A.pop(0)
        A.pop(1-1)
        print('Введите первое число: ')
        A.append(int(input()))
        print('Введите второе число: ')
        A.append(int(input()))
        print(A)

    def task5_3():
        print("Задание 5.3")
        my_len = [["БО-331101", ["Акулова Алена", "Бабушкина Ксения"]], ["БО-402000", ["Капитанов Евгений", "Борисов Александр"]]]
        group = 'БО-402000'
        for i in my_len:
            if group in i[0]:
                print(i[0].center(35))
        for j in i[1]:
                print(j.center(35))


    def task5_4():
        print("Задание 5.4")
        my_len = [["БО-331101", ["Акулова Алена", "Бабушкина Ауения"]], ["БО-402000", ["Капитанов Евгений", "Борисов Александр"]]]
        for i in my_len:
                for j in i[1]:
                    if j[0] == 'А':
                        print(i[0], j)
    task5_1()
    task5_2()
    task5_3()
    task5_4()

def main():
    def menu() -> str:
        choice = str(input('Введите номер задания, которое хотите выполнить:'
                           '\n1 - №1'
                           '\n2 - №2'
                           '\n3 - №3'
                           '\n4 - №4'
                           '\n5 - №5'
                           '\nДля выхода нажмите "0"'
                           '\n-->'))
        return choice

    while True:
        choice = menu()
        if choice == '1':
            task_1()
            choice = menu()
        if choice == '2':
            task_2()
            choice = menu()
        if choice == '3':
            task_3()
            choice = menu()
        if choice == '4':
            task_4()
            choice = menu()
        if choice == '5':
            task_5()
            choice = menu()
        if choice.lower() == '0':
            print('Заверешение программы...')
            break


main()

