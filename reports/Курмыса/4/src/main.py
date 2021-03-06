from random import randint

# Задание 1.1 - нахождение значения функции по параметрам
def task_1_1():
  print('\nДана функция |((a^2-b^3 - c^3*a^2)*(b-c+c*(k-d/b^3))-(k/b-k/a)*c)^2 - 20000|.')
  a, b, c, d, k = list(map(float, input('Введите параметры a, b, c, d, k (a, b != 0): ').split()))
  if a * b == 0:
    print('Деление на ноль воспрещено!\n')
  else:
    print(abs(((a*a / (b**3) + c**3 * a*a) * (b - c + c * (k - d / (b**3)))) - (k / b - k / a * c)**2 - 20000), end='\n\n')

# Задание 1.2 - нахождение нечётных элементов в списке
def task_1_2():
  l = [19, 6, 38, 'ms(PZS*SXsu', 27, 9, 66, '2&8Lnt3c&q', 99, 't#Eavz', 97, '*Fj#mi%tKPayi', 51, 45, 'hHT#AeQ*S*MM#246', 'QuXpiBBfJkQSsKco', 51, 'RqUBECOUEKvETvhr', 98, 'gAH%pMMUw##pHJm', 83, 'sHs08y1uV6Or9', '2W59udOnK', 'qv8rfV4m02', 9, '8J5MNy#Y2E)6Jg*', 26, 'ahtHhBUIEvaoxHvW', 3, 'xk6P5)XZ0#o', 'ZxMGDq', 15, '7*%AB98V', 'BndpoLtjsIwxvuT', 96, '9CkkLi#)1eV', '9G28ev(', '#MQ9y*e7WVSc)0x', '*d(CPaqBbM%#gRuU', 'GpzLpXuyWD', 'zbznrUsMd', 'FOy1ip1qW65Bh0', 'x9f8sMz2XZ5', 'ZVWwKj%', 'bsguivasnPN', 47, 43, 'UJmyjaLPIFkk', 'zeAOOruqdWC', 'aUJUwkqRSxVucbro', 'WJenLtAF', 50, 'oxEuJxWeagEvx', 'ENe*6m22##7B1(zp', 'QV(yvfliYf)']
  print('\nДан список', l)
  print('Нечётные элементы списка: ', end = '')
  for i in range(1, len(l), 2):
    print(l[i], end = ' ')
  print('\n')

# Задание 1.3 - нахождение суммы чисел от 1 до 10 из списка
def task_1_3():
  l = list(map(int, "86 -46 96 96 100 -66 9 -68 -98 -83 -35 52 -3 82 72 25 73 -100 -42 -9 -85 66 88 57 -73 -67 -93 54 64 43 98 5 61 81 -65 -62 14 46 -24 -22 -33 20 90 -63 40 -73 -26 64 -84 -24 82 -97 27 -22 -76 67 -80 82 -95 -63 -64 -16 -94 -71 71 -95 45 -55 38 -94 -65 -68 -9 -77 -79 59 -30 -39".split()))
  print('\nДан список чисел: ', l)
  S = 0

  for i in l:
    if 1 <= i <= 10:
      S += i

  print('Сумма чисел от 1 до 10:', S, end='\n\n')

# Задание 1.4 - нахождение минимума списка
def task_1_4():
  l = list(map(int, "-27 19 -31 -24 -82 -99 24 59 -81 59 62 -61 -64 47 -61 -100 73 26 91 -83 -53 -93".split()))
  print('\nДан список', l)
  print('Минимальное число списка = ', min(l))

# Задание 2.1 - ввод чисел до тех пор, пока оно не будет равно изначально сгенерированному числу
def task_2_1():
  my_number = randint(1, 100)
  print('\nЧисло my_number равно', my_number)
  while True:
    user_number = int(input('Введите число user_number такое, что user_number = my_number: '))
    if user_number != my_number:
      break
  print('Вы ввели число, не равное my_number!\n')

# Задание 2.2 - нахождение строк с длиной < 10
def task_2_2():
  l = ['vfnjk', 'cndbjehvcbje', 'cnejkc', 'ncwubce', 'cmkwednv', 'nvbeyjrkc', 'mkwnkel', 'keocljik', 'cwndbj', 'cnwksedjk', 'nwcjhvjhbkdlw', 'nkecndmlsijh', 'cnwbjvsbnilrkjf', 'mncebduijvutrfi', 'cenk']
  print('\nДан список строк', l)
  print('Строки с длиной < 10: ', end='')
  for i in l:
    if len(i) < 10:
      print(i, end=' ')

# Задание 2.3 - вывод строк с N символами 'R'
def task_2_3():
  N = int(input('Введите длину строки: '))
  print('R' * N)

# Задание 2.4 - создание из строки новой, но только с буквами
def task_2_4():
  str = 'Gs5Ru&C4#Q**Fv430#*&#NKs934R9lLd)c4W1&E&d#mq53CC55kiM(k#Gt7g)%9Vu)5k7*0US2)2)OpQ57R9Bl#T&4qhc)i%4u*PG3&5dA%#4FveT)cJ#41&Ln)gI303L0&VN7*Kn0%LjSA(8*F3h%nk#Vz49pf*'
  print('\nДана строка', str)
  print('Эта же строка, содержащая только буквы: ', end='')
  for i in str:
    if i.isalpha():
      print(i, end='')

# Матрица для заданий 3.X
matrix = [
  [1, 2, 3, 4, 5, 6, 7, 8],
  [8, 7, 6, 5, 4, 3, 2, 1],
  [2, 3, 4, 5, 6, 7, 8, 9],
  [9, 8, 7, 6, 5, 4, 3, 2],
  [1, 3, 5, 7, 9, 7, 5, 3],
  [3, 1, 5, 3, 2, 6, 5, 7],
  [1, 7, 5, 9, 7, 3, 1, 5],
  [2, 6, 3, 5, 1, 7, 3, 2]
]

def show_matrix():
  print('\nДана следующая матрица:')
  for i in matrix:
    for j in i:
      print(j, end=' ')
    print()

def task_3_1():
  show_matrix()
  print('\nМатрица после возведения всех чётных элементов в квадрат:')
  for i in matrix:
    for j in i:
      print(j**(2 - j % 2), end = ' ')
    print()
  print()

def task_3_2():
  show_matrix()
  N = int(input('\nВведите столбец, сумму которого Вы хотите подсчитать (от 1 до 8): '))
  if not(1 <= N <= 8):
    print('Вы вышли за пределы интервала!')
    return
  S = 0
  for i in matrix:
    S += i[N - 1]
  print('Сумма элементов в столбце №', N, 'равна', S, end='\n\n')

def task_3_4():
  show_matrix()
  S = 0
  for i in matrix:
    for j in i:
      S += j
  print('\nСумма всех элементов матрицы равна', S, end='\n\n')

def task_3_5():
  show_matrix()
  N = int(input('\nВведите число, на которое нужно заменить все меньшие его элементы матрицы: '))
  print('Матрица после изменения:')
  for i in matrix:
    for j in i:
      print(j if j >= N else N, end=' ')
    print()
  print()

def task_3_6():
  show_matrix()
  N = int(input('\nВведите номер столбца, который нужно удалить из матрицы (от 1 до 8): '))
  if not(1 <= N <= 8):
    print('Вы вышли за пределы интервала!')
    return
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if j != N - 1:
        print(matrix[i][j], end=' ')
    print()
  print()

def task_3_7():
  N, M = map(int, input('\nВведите измерения для новой матрицы, заполненной нулями: ').split())
  new_matrix = [[0] * M] * N
  print('Сгенерированная матрица:')
  for i in new_matrix:
    for j in i:
      print(j, end=' ')
    print()
  print()

def task_3_8():
  show_matrix()
  N = int(input('\nВведите номер строки, элементы которой нужно ввести, возведя их в квадрат (от 1 до 8): '))
  if not(1 <= N <= 8):
    print('Вы вышли за пределы интервала!')
    return
  print('Элементы строки в квавдрате: ', end='')
  for j in matrix[N - 1]:
    print(j*j, end= ' ')

def task_4_1():
  s = 'Лилибет лила воду, Лиза лизала мороженое, Ли оформлял лизинг на машину, а фокусник уехал в Лиму.'
  print('\nДана строка:', s)
  s = s.split()
  print('Все слова данной строки, начинающиеся на "ли": ', end='')
  for word in s:
    if word[:2].lower() == 'ли':
      for letter in word:
        if not letter.isalpha():
          break
        print(letter, end='')
      print(end=', ')

def task_4_2():
  s = 'ФИО;Возраст;Категория_Иванов Иван Иванович;23 года;Студент 3 курса_Петров Семён Игоревич;22 года;Студент 2 курса'.split('_')
  for i in range(len(s)):
    s[i] = s[i].split(';')
    print("{0:25} {1:15} {2:15}".format(s[i][0], s[i][1], s[i][2]))

def task_4_3():
  s = "ФИО;Возраст;Категория_Иванов Иван Иванович;23 года;Сnудент 3 курса_Петров Семён Игоревич;22 года;Студент 2 курса_Иванов Семён Игоревич;22 года;Студент 2 курса_Акибов Ярослав Наумович;23 года;Студент 3 курса_Борков Станислав Максимович;21 год;Студент 1 курса_Петров Семён Семёнович;21 год;Студент 1 курса_Романов Станислав Андреевич;23 года;Студент 3 курса_Петров Всеволод Борисович;21 год;Студент 2 курса".split('_')
  for i in range(len(s)):
    s[i] = s[i].split(';')
    if i == 0 or s[i][1] == '21 год':
      print("{0:30} {1:15} {2:15}".format(s[i][0], s[i][1], s[i][2]))

def task_4_4():
  s = '''Научно-фантастический рассказ
Тема: «Почему необходимо и достаточно соединение?»
Понятие модернизации экономит сенсибельный постиндустриализм, и здесь в качестве модуса конструктивных элементов используется ряд каких-либо единых длительностей. Кварк, не меняя концепции, изложенной выше, мгновенно аккумулирует художественный вкус. Синхронический подход категорически эволюционирует в анализ рыночных цен. Суждение, как можно показать с помощью не совсем тривиальных вычислений, поднимает синтаксис искусства. Тем не менее, феномен толпы заставляет комплексный склон Гиндукуша.

Ролевое поведение заканчивает диктат потребителя. Делькредере последовательно. При погружении в жидкий кислород метафора качественно формирует оз. Многочисленные расчеты предсказывают, а эксперименты подтверждают, что туффит умышленно подрывает кварц. Эпическая медлительность, особенно в условиях политической нестабильности, инструментально обнаружима. Ведущий экзогенный геологический процесс - гомеостаз интуитивно понятен.

Под воздействием переменного напряжения реформаторский пафос отображает астатический суглинок. Туманность Андромеды пространственно дает архетип. Болгария щелочно нивелирует термальный источник. Художественная богема отталкивает стремящийся хорал, учитывая, что в одном парсеке 3,26 световых года. Рекламная заставка, на первый взгляд, образует межагрегатный нишевый проект.''' # Яндекс.Рефераты форевер :D
  print('\nТекст:\n', s, '\nДлина текста:', len(s), '\nКоличество слов в нём:', len(s.split()))

def task_6_1():
  N = int(input('\nВведите размерность для новой матрицы: '))
  S = 0
  print('Сгенерированная матрица:')
  matrix = []
  for i in range(N):
    matrix.append([])
    for j in range(N):
      matrix[i].append(randint(-100, 100))
      S += matrix[i][j]
      print(matrix[i][j], end=' ')
    print()
  print('Сумма всех элементов матрицы равна', S)

def task_6_2():
  l = [randint(-100, 100) for i in range(10)]
  print('\nИзначальный список:', l)
  i = 0
  while i < len(l):
    if l[i] % 2 == 0:
      del l[i]
    else:
      i += 1
  l.extend([42, 69])
  print('Список после изменений:', l)

def task_6_3():
  students = [['БО-331101', ['Уваров Даниил', 'Романенко Инга', 'Павлив Емельян']], ['БОВ-421102', ['Кириллова Шанетта', 'Захарова Ярослава', 'Тарасюк Ева', 'Колесник Никодим', 'Родионова Злата', 'Кличко Евгений', 'Хованска Чара', 'Цветкова Марта', 'Бондаренко Добрыня']], ['БО-331103', ['Тарасова Йана', 'Тетеров Устин', 'Русакова Анжелика', 'Панфилова Ульяна', 'Петрова Оксана', 'Пасичник Эрик', 'Мухина Йосифа']]]
  group = input('\nВведите название группы: ')
  for i in students:
    if i[0] == group:
      print(group, ": ", end='')
      for student in i[1]:
        print(student, end=', ')
  print('\n\nВывод студентов группы завершён либо такой группы здесь нет!')

def task_6_4():
  students = [['БО-331101', ['Уваров Даниил', 'Романенко Инга', 'Павлив Емельян']], ['БОВ-421102', ['Кириллова Шанетта', 'Захарова Ярослава', 'Тарасюк Ева', 'Колесник Никодим', 'Родионова Злата', 'Кличко Евгений', 'Хованска Чара', 'Цветкова Марта', 'Бондаренко Добрыня']], ['БО-331103', ['Тарасова Йана', 'Тетеров Устин', 'Русакова Анжелика', 'Панфилова Ульяна', 'Петрова Оксана', 'Пасичник Эрик', 'Мухина Йосифа']]]
  print('\nСписок студентов, у которых в фамилии имеется менее 7 букв: ')
  for group in students:
    for student in group[1]:
      if student.find(' ') < 7:
        print(student, ', группа - ', group[0], sep='')

while True:
  x = int(input('Выберите номер задания (от 1 до 6, кроме 5) или 0, если Вы хотите вы выйти из программы: '))
  if x == 0:
    print('Производится выход из программы...')
    break
  elif x == 1:
    print('\nЗадание 1\n')
    y = int(input('0 - Выход из программы\n1 - Нахождение значения функции по параметрам\n2 - Вывод нечётных элементов списка по индексам\n3 - Сумма чисел от 1 до 10 из списка\n4 - Нахождение минимума списка\n'))
    if y == 0:
      print('Производится выход из программы...')
      break
    elif y == 1:
      task_1_1()
    elif y == 2:
      task_1_2()
    elif y == 3:
      task_1_3()
    elif y == 4:
      task_1_4()
    else:
      print('Некорректный номер пункта!')
  elif x == 2:
    print('\nЗадание 2 "Списки и строки"\n')
    y = int(input('0 - Выход из программы\n1 - Ввод числа до его неравенства с указанным\n2 - Вывод строк с длиной меньше 10 символов\n3 - Вывод N-символьной строки из \'R\'\n4 - Создание новой строки, состоящей из букв старой строки'))
    if y == 0:
      print('Производится выход из программы...')
      break
    elif y == 1:
      task_2_1()
    elif y == 2:
      task_2_2()
    elif y == 3:
      task_2_3()
    elif y == 4:
      task_2_4()
    else:
      print('Некорректный номер пункта!')
  elif x == 3:
    print('\nЗадание 3 "Матрицы"\n')
    y = int(input('0 - Выход из программы\n1 - Возведение чётных элементов в квадрат\n2 - Сложение по столбцам\n3 - отсутствует\n4 - Сложение всех элементов матрицы\n5 - Замена всех элементов на введённое число, большее их\n6 - Удаление стоолбца из матрицы\n7 - Создание матрицы из нулей\n8 - Вывод элементов строки матрицы в квадрате'))
    if y == 0:
      print('Производится выход из программы...')
      break
    elif y == 1:
      task_3_1()
    elif y == 2:
      task_3_2()
    elif y == 4:
      task_3_4()
    elif y == 5:
      task_3_5()
    elif y == 6:
      task_3_6()
    elif y == 7:
      task_3_7()
    elif y == 8:
      task_3_8()
    else:
      print('Некорректный номер пункта!')
  elif x == 4:
    print('\nЗадание 4 "Строки"\n')
    y = int(input('0 - Выход из программы\n1 - Нахождение слов, начинающихся на "Ли"\n2 - Вывод информации через таблицу\n3 - Вывод информации через таблицу с условием\n4 - Анализ текста (слова, символы)'))
    if y == 0:
      print('Производится выход из программы...')
      break
    elif y == 1:
      task_4_1()
    elif y == 2:
      task_4_2()
    elif y == 3:
      task_4_3()
    elif y == 4:
      task_4_4()
    else:
      print('\Некорректный номер пункта!')
  elif x == 6:
    print('\nЗадание 6 "Списки"\n')
    y = int(input('0 - Выход из программы\n1 - Матрица как списка, сумма всех её элементов\n2 - Удаление и добавление элементов матрицы\n3 - Вывод информации из списка с условием по группе\n4 - Вывод информации из списка с условием по фамилии'))
    if y == 0:
      print('Производится выход из программы...')
      break
    elif y == 1:
      task_6_1()
    elif y == 2:
      task_6_2()
    elif y == 3:
      task_6_3()
    elif y == 4:
      task_6_4()
    else:
      print('\Некорректный номер пункта!')
  else:
    print('\nНекорректный входной параметр!\n')
  x = input('\nЖелаете продолжить выполнение программы? (введите либо 1, либо "yes", либо "да", либо "y") ')
  if not(x == '1' or (x.lower() in ['да', 'yes', 'y'])):
    print('Производится выход из программы...')
    break 
