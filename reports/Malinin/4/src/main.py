# 1
def task_1():
    def task_1_1():
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

    def task_1_2():
        a = [300, "haha", 1488, "bymbym", 228, "kaka", 1337, "yep", 1, "gg"]
        for i in range(len(a)):
            if i % 2 == 1:
                print(a[i])

    def task_1_3():
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        x = 1
        for i in a:
            if i > 10:
                x = x * i
        print(x)

    def task_1_4():
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        i = len(a) // 2
        print(a[i])

    task_1_1()
    task_1_2()
    task_1_3()
    task_1_4()


# 2
def task_2():
    def task_2_1():
        a = 7
        while True:
            x = int(input("Введите число: "))
            if x < a:
                break

    def task_2_2():
        a = ['spam', 'road', 'ham', 'red']

        for i in a:
            if i[0] == 'r':
                print(i)

    def task_2_3():
        import string
        import random

        some_str = ''
        some_seq = string.ascii_letters + string.digits

        for i in range(8):
            some_str += random.choice(some_seq)

        if some_str.isalpha():
            some_str[int(random.randint(0, 7))] = random.choice(string.digits)

        print(some_str)

    def task_2_4():
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

    task_2_1()
    task_2_2()
    task_2_3()
    task_2_4()


# 3
def task_3():
    def task_3_1():
        print('Задание 3.1')
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        lines = 4
        for i in range(lines):
            for j in range(8):
                matrix[i][j] = matrix[i][j] ** 2
        print(*matrix, sep='\n')

    def task_3_2():
        print('\nЗадание 3.2')
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        result_list = []
        for j in range(1, 8, 2):
            res_sum = 0
            for i in range(8):
                res_sum += matrix[i][j]
            if res_sum != 0:
                result_list.append(res_sum)
        print(result_list)

    def task_3_4():
        print('\nЗадание 3.4')
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        matrix = [[0] * 8] * 8
        print(*matrix, sep='\n')

    def task_3_5():
        print('\nЗадание 3.5')
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 5: matrix[i][j] = matrix[i][j] ** 2
        print(*matrix, sep='\n')

    def task_3_6():
        print('\nЗадание 3.6')
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        matrix = [[0] * 8] * 8
        print(*matrix, sep='\n')
        # del matrix

    def task_3_7():
        print('\nЗадание 3.7')
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        a = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 3: a += 1
        print("Число 3 встречается в матрице ", a, "раз.")

    task_3_1()
    task_3_2()
    task_3_4()
    task_3_5()
    task_3_6()
    task_3_7()


# 4
def task_4():
    def task_4_1():
        print('Задание 4.1')
        import re
        test_string = 'Петров и Иванов, а еще Игоренко собрались поехать во Львов!'
        split_string = re.split(' |,|!', test_string)
        result_string = ''
        for i in split_string:
            if i.find('ов') != -1:
                result_string = result_string + i + ' '
        print(result_string)

    def task_4_2():
        print('\nЗадание 4.2')
        my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;2    3 года;Студент 3 курса;' \
                    '_Петров;Семен;Игоревич;22 года;Студент 2 курса'
        my_list = [str.split(';') for i, str in enumerate(my_string.split('_')) if i > 0]
        print('ФИО \t\t\t\t\tО студенте')
        for element in my_list:
            print(element[0], element[1], element[2], element[4].rjust(18) + ',', element[3])

    def task_4_3():
        print('\nЗадание 4.3')
        my_string = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;' \
                    '_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года; Студент 2 курса;' \
                    '_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;' \
                    '_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса' \
                    '_Петров Всеволод Борисович;21 год;Студент 2 курса'
        my_list = [str.split(';') for i, str in enumerate(my_string.split('_')) if i > 0]
        print('ФИО\t\t\t\t\t\t\t\tВозраст\t\tКатегория')
        counter = 0
        for element in my_list:
            if element[0].startswith('А') or element[0].startswith('Б'):
                print(element[0].ljust(31), element[1].ljust(11), element[2])

    def task_4_4():
        print('\nЗадание 4.4')
        import string
        my_string, count = 'I love friday and clouds very much you', 0
        for i in my_string:
            if string.ascii_letters.find(i) != -1:
                count += 1
        amount_words = len(my_string.split(' '))
        print('Количество символов в строке:', count)
        print('Количество слов в строке:', amount_words)

    task_4_1()
    task_4_2()
    task_4_3()
    task_4_4()


# 6
def task_5():
    import random
    def task_5_1():
        print('Задание 5.1')

        def print_matrix(matrix):
            for i in range(size):
                for j in range(size):
                    print('{:3d}'.format(matrix[i][j]), end=' ')
                print()

        size = int(input('Введите размерность матрицы (N): '))
        matrix = []
        my_list = []
        for i in range(0, size):
            matrix.append([])
            for j in range(0, size):
                matrix[i].append(random.randint(0, 10))
                my_list.append(matrix[i][j])
        sum = 0
        for k in my_list:
            sum += k
        print_matrix(matrix)
        print('Список из матрицы:', my_list)
        print('Результат сложения всех элементов матрицы:', sum)

    def task_5_2():
        print('\nЗадание 5.2')
        my_list = []
        for j in range(10):
            my_list.append(random.randint(0, 50))
        print('Исходный список:', my_list)
        for i in range(5):
            my_list.append(int(input('Введите новый элемент списка: ')))
        print('Список после добавления новых элементов:', my_list)
        result_string = []
        for element in my_list:
            if element % 2 == 1:
                result_string.append(element)
        print('Итоговый список, состоящий из нечётных элементов:', result_string)

    def task_5_3():
        print('\nЗадание 5.3')
        my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения']],
                  ['БОВ-421102', ['Кузьмин Артём', 'Прокофьев Максим']],
                  ['БО-331103', ['Тарасов Иван', 'Егоров Герман']]]
        print('Название группы\t\t\tФИО\t\t\t\tФИО')
        for element in my_len:
            if element[0].startswith('БО-'):
                print(element[0].ljust(17), element[1][0].ljust(15), element[1][1])

    def task_5_4():
        print('\nЗадание 5.4')
        my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения', 'Баженов Максим', 'Лапина Мелания']],
                  ['БОВ-421102', ['Кузьмин Артём', 'Прокофьев Максим', 'Тарасов Алексей', 'Грачев Александр']],
                  ['БО-331103', ['Тарасов Иван', 'Егоров Герман', 'Румянцев Матвей', 'Архипов Тимофей']]]
        print('Студент\t\t\t\t\tГруппа')
        for groups in my_len:
            for counter, student in enumerate(groups[1]):
                if counter % 2 == 0:
                    print(student, groups[0].rjust(18))

    task_5_1()
    task_5_2()
    task_5_3()
    task_5_4()


def main():
    def menu() -> str:
        choice = str(input('Введите номер задания, которое хотите выполнить:'
                           '\n1 - №1'
                           '\n2 - №2'
                           '\n3 - №3'
                           '\n4 - №4'
                           '\n5 - №5'
                           '\nДля выхода нажмите "t"'
                           '\n-->'))
        return choice

    while True:
        func = {
            '0': exit,
            '1': task_1,
            '2': task_2,
            '3': task_3,
            '4': task_4,
            '5': task_5
        }
        func[menu()]()
        # choice = menu()
        # if choice == '1':
        #     task_1()
        #     choice = menu()
        # if choice == '2':
        #     task_2()
        #     choice = menu()
        # if choice == '3':
        #     task_3()
        #     choice = menu()
        # if choice == '4':
        #     task_4()
        #     choice = menu()
        # if choice == '5':
        #     task_5()
        #     choice = menu()
        # if choice == '6':
        #     task_5()
        #     choice = menu()
        # if choice == '7':
        #     task_5()
        #     choice = menu()
        # if choice.lower() == 't':
        #     print('Заверешние программы...')
        #     break


main()
