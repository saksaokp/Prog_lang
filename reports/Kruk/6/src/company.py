class Company:
    count = 0
    __name = str()
    __workers = int()
    __year = int()

    def __init__(self):
        Company.count += 1
        print(Company.count)
        print('Конструктор без параметров класса Company')

    def __init__(self, nm="", wrs=0, ye=0):
        Company.count += 1
        print(Company.count)
        try:
            self.__name = nm
            self.__workers = wrs
            self.__year = ye
        except ValueError as e:
            print(e)
        print('Конструктор с параметрами класса Company')

    def __del__(self):
        print('Дестрктор класса Company')

    def setname(self, nm):
        self.__name = nm

    def setworkers(self, wrs):
        self.__workers = wrs

    def setdate(self, ye):
        self.__year = ye

    def getname(self):
        return self.__name

    def getworkers(self):
        return self.__workers

    def getyears(self):
        return self.__year

    def write(self):
        try:
            self.__name = str(input("Введите название компании: "))
            self.__workers = int(input("Введите количество сотрудников: "))
            self.__year = int(input("Введите год основания компании: "))
        except ValueError:
            print("Не верный ввод!")

    def show(self):
        print(
            "\nНазвание компании: " + self.__name + "\nКоличество сотрудников: " + str(
                self.__workers) + "\nГод основания:  " + str(self.__year))