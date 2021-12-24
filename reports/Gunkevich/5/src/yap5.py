import os, csv


def task_1():
   files = os.listdir("D:/folder")
   print('Folder содержит файлы: ', files)
   print('Количество файлов: ', len(files))


def task_2():
    students = read()
    students.sort(key=sort_num)
    print("Сортировка по номеру группы:")
    output(students)
    writer(students)
    students.clear


def writer(arr):
    f = open("students.csv", "w", newline="")
    writer = csv.writer(f)
    for i in arr:
        line = [';'.join(i)]
        writer.writerow(line)
    f.close()


def output(arr):
    print("№ ФИО \t Возраст Группа")
    for i in arr:
        for j in range(len(i)):
            if i[j] == "№": break
            print(i[j], end=" ")
        print()
    print()


def read():
    f = open("students.csv", "r")
    reader = csv.reader(f)
    arr = []
    for i in reader:
        arr.append(str(i)[2:len(i) - 3].split(';'))
    f.close()
    print("Исходные данные: ", arr)
    output(arr)
    return arr


def writer5(arr, file_name):
    name = file_name + ".csv"
    f = open(name, "w", newline="")
    writer = csv.writer(f)
    for i in arr:
        line = [';'.join(i)]
        writer.writerow(line)
    f.close()


def read5(file_name):
    name = file_name + ".csv"
    f = open(name, "r")
    reader = csv.reader(f)
    arr = []
    for i in reader:
        arr.append(str(i)[2:len(i) - 3].split(';'))
    f.close()
    return arr


def sort_num(i):
    return i[3]


def task_3():
    students = read()
    num_group = input("Введите номер группы: ")
    for i in range(len(students)):
        if students[i][3] == num_group:
            students[i][2] = str(int(students[i][2]) + 1)
    print("Новый список:\n ", students)
    output(students)
    writer(students)
    students.clear


def task_5():
    file_name = input("Введите название файла:")
    count = int(input("Введите кол-во студентов:"))
    zero = []
    writer5(zero, file_name)
    for i in range(count):
        number = input("Введите номер:")
        name = input('Введите имя:')
        age = input("Введите возраст:")
        num_group = input("Введите номер группы: ")
        arr = [number, name, age, num_group]
        students = read5(file_name)
        students.append(arr)
        writer5(students, file_name)
    students = read5(file_name)
    print("Новый список:\n ", students)
    output(students)
    writer5(students, file_name)
    students.clear


def task_4():
    file_name = input("Введите название файла:")
    arr = read5(file_name)
    output(arr)


def main():
    while True:
        print("Задание 1 - 1")
        print("Задание 2 - 2")
        print("Задание 3 - 3")
        print("Считать из отдельного файла - 4")
        print("Записать в отдельный файл - 5")
        a = int(input("Введите номер задания или 0 для выхода:"))
        if a == 1:
            task_1()
        elif a == 2:
            task_2()
        elif a == 3:
            task_3()
        elif a == 5:
            task_5()
        elif a == 4:
            task_4()
        elif a == 0: break
        else: print("НЕПРАВИЛЬНЫЙ ВВОД!")


main()
