import os, csv

def task_1():
    print('В папке "files" располагается', len(os.listdir('files/')), 'файл(а/ов).')

def output_table(table):
    print('\nСписок студентов:')
    print("{0:4}{1:25}{2:10}{3:10}".format("№", "ФИО", "Возраст", "Группа"))
    for row in table:
        print("{0:4}{1:25}{2:10}{3:10}".format(row[0], row[1], row[2], row[3]))

def task_2():
    f = open("files/students.csv", "r+")
    csv_f = csv.reader(f)
    students = []
    i = 0
    for row in csv_f:
        if i > 0:
            students.append(row)
        i += 1
    students.sort(key=lambda x: int(x[2]))
    output_table(students)
    choice = input('\nЖелаете уменьшить возраст некоторых учащихся на 1? [y/yes/да/1 - да, иначе - нет]\n').lower()
    if choice in ['y', 'yes', 'да', '1']:
        while True:
            N = input('Выберите одну из групп: ')
            for i in range(len(students)):
                if students[i][3] == N:
                    students[i][2] = str(int(students[i][2]) - 1)
            choice = input('\nЖелаете продолжить выполнение функции? [y/yes/да/1 - да, иначе - нет]\n').lower()
            if choice not in ['y', 'yes', 'да', '1']:
                break
        output_table(students)
        choice = input('\nЖелаете сохранить данные файла? [y/yes/да/1 - да, иначе - нет]\n').lower()
        if choice in ['y', 'yes', 'да', '1']:
            f.seek(0)
            f.truncate()
            writer = csv.writer(f)
            writer.writerow(["№", "ФИО", "Возраст", "Группа"])
            students.sort(key=lambda x: int(x[0]))
            for student in students:
                writer.writerow(student)
            print('\nФайл успешно перезаписан!')
    f.close()

def task_3():
    file_name = input('Введите имя файла, которое Вы будете использовать: ').lower()
    with open(f"files/{file_name}.csv", "a+") as f:
      count_of_strings = 0
      option = int(input('Выберите один из предложенных пунктов либо введите 0, чтобы выйти из функции:\n1 - Запись в файл;\n2 - Чтение из файла\n'))
      if option == 0:
        print('\nПроизводится выход из функции...')
      elif option == 1:
        writer = csv.writer(f)
        writer.writerow(["№", "ФИО", "Возраст", "Группа"])
        while True:
          fio = input("Введите ФИО учащегося: ")
          age = input("Введите возраст учащегося: ")
          group_name = input("Введите группу учащегося: ")
          count_of_strings += 1
          writer.writerow([str(count_of_strings), fio, age, group_name])
          choice = input('\nЖелаете продолжить выполнение функции? [y/yes/да/1 - да, иначе - нет]\n').lower()
          if choice not in ['y', 'yes', 'да', '1']:
            break
      elif option == 2:
        f.seek(0)
        csv_f = csv.reader(f)
        for row in csv_f:
          print(','.join(row))
      else:
        print('Некорректный входной параметр!')

print('Лабораторная работа №5:\nФайловая система Python')
while True:
  N = int(input('\nВведите номер задания от 1 до 3 либо 0, если Вы хотите выйти из программы:\n1 - Нахождение количества файлов в папке files;\n2 - Работа с существующими csv-файлами;\n3 - Работа с пользовательскими csv-файлами\n'))
  if N == 0:
    print('\nПроизводится выход из программы...\n')
    break
  elif N == 1:
    task_1()
  elif N == 2:
    task_2()
  elif N == 3:
    task_3()
  else:
    print('\nНекорректный параметр!\n')