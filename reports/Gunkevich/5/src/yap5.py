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


def writer5(arr):
    f = open("students2.csv", "w", newline="")
    writer = csv.writer(f)
    for i in arr:
        line = [';'.join(i)]
        writer.writerow(line)
    f.close()


def read5():
    f = open("students2.csv", "r")
    reader = csv.reader(f)
    arr = []
    for i in reader:
        arr.append(str(i)[2:len(i) - 3].split(';'))
    f.close()
    print("Исходные данные: ", arr)
    output(arr)
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
    students = read()
    writer5(students)


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
            read5()
        elif a == 0: break
        else: print("НЕПРАВИЛЬНЫЙ ВВОД!")


main()