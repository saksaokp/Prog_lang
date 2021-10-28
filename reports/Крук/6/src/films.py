class Films:
    count = 0

    def __init__(self, nm="", wrs=0, ye=0):
        Films.count += 1
        print(Films.count)
        try:
            self._name = nm
            self._fees = wrs
            self._year = ye
        except ValueError as e:
            print(e)
        print('Конструктор с параметрами класса films')

    def __del__(self):
        print('Дестрктор класса films')
        Films.count -= 1

    def setname(self, nm):
        self._name = nm

    def setworkers(self, wrs):
        self._fees = wrs

    def setdate(self, ye):
        self._year = ye

    def getname(self):
        return self._name

    def getworkers(self):
        return self._fees

    def getyears(self):
        return self._year

    def write(self):
        try:
            self._name = str(input("Введите название фильма: "))
            self._fees = int(input("Введите количества сборов фильма: "))
            self._year = int(input("Введите год выхода фильма: "))
        except ValueError:
            print("Не верный ввод!")

    def show(self):
        print(
            "\nНазвание фильма: " + self._name + "\nСборы: " + str(
                self._fees) + "\nГод выхода:  " + str(self._year))