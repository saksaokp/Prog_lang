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
