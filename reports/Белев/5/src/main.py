import os
import csv


def T1():
    print(len(os.listdir(path=".")))


def name_key(name): return name[1]


def T2():
    students = []
    r_file = open("students.csv", encoding='utf-8')
    file_reader = csv.reader(r_file, delimiter=";")
    row_count = 0
    for row in file_reader:
        students.append([])
        for i in range(4):
            students[row_count].append(f'{row[i]}')
        row_count += 1
    r_file.close()
    students.sort(key=name_key)
    print(students)
    while True:
        print("Чтобы увеличить возраст всех студентов введите +")
        print("Чтобы сохранить данные в файл введите s")
        move = input()
        if move == '+':
            for row in students:
                if row[2] != "Возраст":
                    row[2] = int(row[2]) + 1
            print(students)
        elif move == 's':
            w_file = open("students.csv", mode="w", encoding="utf-8")
            file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
            for row in students:
                file_writer.writerow(row)
            w_file.close()
        else:
            break


# T1()
T2()
