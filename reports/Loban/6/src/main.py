class Street:
    count = 0
    # Если переменная начинается с двух нижних подчеркиваний, то эта переменная будет доступна только внутри класса
    # Это инкапсуляция (сокрытие данных)

    # Полиморфизм - способность функции обрабатывать данные разных типов.
    __street_name = str()
    __city = str()
    __number = int()

    def __init__(self):
        Street.count += 1
        print(Street.count)

    def __init__(self, sn="", ct="", nm=0):
        Street.count += 1
        print(Street.count)

        print("Конструктор с параметрами вызван")
        try:
            self.__street_name = str(sn)  # __street_name - поле класса
            self.__city = str(ct)
            self.__number = int(nm)
        except ValueError as e:
            print(e)

    def set_street_name(self, sn):
        try:
            self.__street_name = str(sn)
        except ValueError as e:
            print(e)

    def set_city(self, ct):
        try:
            self.__city = str(ct)
        except ValueError as e:
            print(e)

    def set_number(self, nm):
        try:
            self.__number = int(nm)
        except ValueError as e:
            print(e)

    def get_street_name(self):
        return self.__street_name

    def get_city(self):
        return self.__city

    def get_number(self):
        return self.__number

    def read(self):
        try:
            self.__street_name = input("Введите название улицы :\n")
            self.__city = input("Введите название города:\n")
            self.__number = int(input("Введите номер улицы:\n"))
        except ValueError:
            print("Ошибка ввода")

    def show(self):
        print("Название улицы:" + self.__street_name + " Название города:" + self.__city  + " Номер улицы:" + str(self.__number))


# Специальная переменная __name__ будет равна __main__ только, когда запускается как отдельный файл
# Равна имени скрипта, который импортировал этот скрипт
if __name__ == "__main__":
    y = Street()  # Создание экземпляра класса. Вызывается конструктор без параметров
    y1 = Street()
    y.read()
    y1.read()
    y.show()
    y1.show()
    x = Street("Советская", "Брест", 19)
    x.show()
    c = Street()
    c.set_street_name("Московская")
    c.set_city("Брест")
    c.set_number(17)
    c.show()
    print("Количество улиц:", Street.count)
