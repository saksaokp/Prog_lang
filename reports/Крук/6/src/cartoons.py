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