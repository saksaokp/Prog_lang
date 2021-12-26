import os
import csv


def task_1():
    files_and_catalogs = os.listdir("./data")  # ['1', '2', 'TEXT.txt']
    files = []
    catalogs = []
    for element in files_and_catalogs:
        if os.path.isfile('./data/' + element):
            files.append(element)
        else:
            catalogs.append(element)

    print('data содержит файлы: ', files)
    print('Количество файлов: ', len(files))
    print('data содержит папки: ', catalogs)
    print('Количество папок: ', len(catalogs))


def task_2():
    students = read()
    print("Исходные данные:")
    output(students)

    students.sort(key=lambda student: student[3])
    print("Отсортированные данные:")
    output(students)

    writer(students)


def writer(students):
    file = open("students.csv", "w", newline="", encoding='utf-8')
    writer = csv.writer(file, delimiter=';')
    for student in students:
        writer.writerow(student)
    file.close()


def output(students):
    print("[№ ФИО Возраст Группа]")
    for student in students:
        print(student)


def read():
    file = open("./students.csv", "r", encoding='utf-8')
    students = list(csv.reader(file, delimiter=';'))
    file.close()
    return students


def task_3():
    students = read()
    num_group = input("Введите номер группы: ")

    for i in range(len(students)):
        if students[i][3] == num_group:
            students[i][2] = str(int(students[i][2]) - 1)

    print("Новый список:")
    output(students)
    writer(students)


def main():
    while True:
        print("Задание 1 - 1")
        print("Задание 2 - 2")
        print("Задание 3 - 3")
        a = int(input("Введите номер задания или 0 для выхода:"))
        if a == 1:
            task_1()
        elif a == 2:
            task_2()
        elif a == 3:
            task_3()
        elif a == 0:
            break
        else:
            print("НЕПРАВИЛЬНЫЙ ВВОД!")


main()
