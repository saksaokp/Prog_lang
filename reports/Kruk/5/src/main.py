import csv
import os

l = []
s = str()

def files() -> None:
    count = 0
    for root, dirs, fiels in os.walk("venv"):
        count += len(fiels)
    print("\nКолличество файлов в папке:", count)


def open_lines() -> list:
    global l
    file = open('students.csv', 'r', encoding='utf-8')
    lines = file.readlines()
    for ind in range(len(lines)):
        lines[ind] = lines[ind].split(';')
    file.close()
    l = lines
    return lines


def out_age() -> None:
    csv_open()
    lines = l
    print()
    for line in lines[1:]:
        if int(line[2]) > 22:
            print(*line, end="")
            print()


def age_upp():
    global l
    g = input('Введите группу: ')
    for ind in range(len(l)):
        try:
            if g == l[ind][3]:
                l[ind][2] = str(int(l[ind][2]) + 1)
        finally:
            continue
    csv_save()


def save_lines(lines: list):
    file = open('students.csv', 'w', encoding='utf-8')
    for ind in range(len(lines)):
        lines[ind] = ';'.join(lines[ind])
    file.writelines(lines)


def openfile() -> str:
    file = open(input('Введите название файла: '), 'r', encoding='utf-8')
    s = file.read()


def savefile():
    global s
    file = open(input('Введите название файла: '), 'w', encoding='utf-8')
    file.write(s)
    file.close()


def change_file():
    global s
    print("1. Очистить")
    print("2. Приписать в конце")
    com = int(input("Выберите измение: "))
    if (com == 1):
        s = ""
    if (com == 2):
        s += input("Введите в конец: ")


def csv_save():
    global l
    f = open(input('Введите название файла: '), 'w', encoding='utf-8', newline='')
    writer = csv.writer(f, delimiter=';')
    for line in l:
        writer.writerow(line)


def csv_open():
    global l
    f = open(input('Введите название файла: '), 'r', encoding='utf-8')
    reader = csv.reader(f, delimiter=';')
    l = []
    for row in reader:
        l.append(row)
    f.close()


def menu():
    print("\n0. Закрытие программы")
    print("1. Количество файлов в папке venv")
    print("2. Вывод студентов после 22")
    print("3. Увеличение возраста")
    print("4. Открытие файла")
    print("5. Изменить файл")
    print("6. Сохранение файла")


if __name__ == '__main__':
    csv_open()
    func = {
        1: files,
        2: out_age,
        3: age_upp,
        4: openfile,
        5: change_file,
        6: csv_save
    }
    while (True):
        menu()
        com = int(input('Выберите команду: '))
        if (com == 0):
            break
        func[com]()
