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


from films import Films


class TV(Films):
    _channel = str()

    def __init__(self, nm="", wrs=0, ye=0, ch=""):
        super(TV, self).__init__(nm, wrs, ye)
        self._channel = ch
        print('Конструктор класса TV')

    def __del__(self):
        print('Дестрктор класса TV')

    def setchannel(self, ch):
        self._channel = ch

    def getchannel(self):
        return self._channel

    def write(self):
        try:
            self._name = str(input("Введите название телефильма: "))
            self._fees = int(input("Введите количества сборов телефильма: "))
            self._year = int(input("Введите год выхода телефильма: "))
            self._channel = str(input("Введите канал вещания телефильма: "))
        except ValueError:
            print("Не верный ввод!")

    def show(self):
        print(
            "\nНазвание фильма: " + self._name + "\nСборы: " + str(
                self._fees) + "\nГод выхода:  " + str(self._year) + "\nКанал вещания: " + self._channel)


from films import Films


class cartoons(Films):
    _studio = str()

    def __init__(self, nm="", wrs=0, ye=0, st=""):
        super(cartoons, self).__init__(nm, wrs, ye)
        self._studio = st
        print('Конструктор класса cartoons')

    def __del__(self):
        print('Дестрктор класса cartoons')

    def setchannel(self, sc):
        self._studio = sc

    def getchannel(self):
        return self._studio

    def write(self):
        try:
            self._name = str(input("Введите название мультфильма: "))
            self._fees = int(input("Введите количества сборов мультфильма: "))
            self._year = int(input("Введите год выхода мультфильма: "))
            self._studio = str(input("Введите студию мультфильма: "))
        except ValueError:
            print("Не верный ввод!")

    def show(self):
        print(
            "\nНазвание фильма: " + self._name + "\nСборы: " + str(
                self._fees) + "\nГод выхода:  " + str(self._year) + "Студия мультфильма: " + self._studio)
