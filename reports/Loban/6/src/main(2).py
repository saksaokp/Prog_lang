class Human:
    name = str()

    def __init__(self, nm=""):
        print("Вызван конструктор Human", self)
        if type(nm) == str:
            self.__name = nm
        else:
            print("Ошибка ввода")

    def set_name(self, nm):
        if type(nm) == str:
            self.__name = nm
        else:
            print("Ошибка ввода")

    def get_name(self):
        return self.__name

    def __del__(self):
        print("Вызван деструктор класса Human ", self)

    def read(self):
        self.__name = input("Введите имя человека:\n")

    def show(self):
        print("Имя человека:", self.__name)


class Serviceman(Human):
    __place_of_service = str()

    def __init__(self, ps="", nm=""):
        print("Вызван конструктор класса Serviceman", self)
        try:
            self.__place_of_service = ps
            self.__name = nm
        except ValueError:
            print("Ошибка ввода")

    def set_place_of_service(self, ps):
        self.__place_of_service = ps

    def get_place_of_service(self):
        return self.__place_of_service

    def __del__(self):
        print("Вызван деструктор класса Serviceman", self)

    def read(self):
        self.__name = input("Введите имя военнослужащего:\n")
        self.__place_of_service = input("Введите место службы:\n")

    def show(self):
        print("Имя человека: ", self.__name)
        print("Место службы: ", self.__place_of_service)


class Officer(Serviceman):
    __number_of_subordinates = int()

    def __init__(self, ps="", nm="", ns=0):
        print("Вызван конструктор класса Officer", self)
        try:
            self.__name = nm
            self.__place_of_service = ps
            self.__number_of_subordinates = int(ns)
        except ValueError:
            print("Ошибка ввода")

    def __del__(self):
        print("Вызван деструктор класса Officer", self)

    def set_number_of_subordinates(self, ns):
        try:
            self.__number_of_subordinates = ns
        except ValueError:
            print("Ошибка ввода")

    def get_number_of_subordinates(self):
        return self.__number_of_subordinates

    def read(self):
        try:
            self.__name = input("Введите имя военнослужащего:\n")
            self.__place_of_service = input("Введите место службы:\n")
            self.__number_of_subordinates = int(input("Введите количество подчиненных:\n"))
        except ValueError:
            print("Ошибка ввода")

    def show(self):
        print("Имя человека: ", self.__name)
        print("Место службы: ", self.__place_of_service)
        print("Количество подчиненных:", self.__number_of_subordinates)


if __name__ == '__main__':
    print("Example 1")
    human1 = Human()
    human1.set_name("Олешик Максим")
    human1.show()
    print("\n")

    print("Example 2")
    human2 = Human("Теркин Леонид")
    human2.show()
    print("\n")

    print("Example 3")
    serviceman1 = Serviceman()
    serviceman1.read()
    serviceman1.show()
    print("\n")

    print("Example 4")
    serviceman2 = Serviceman("Петров Константин", "д. Нижние холмы")
    serviceman2.show()
    print("\n")

    print("Example 5")
    officer1 = Officer()
    officer1.read()
    officer1.show()
    print("\n")

    print("Example 6")
    officer2 = Officer("Тернов Андрей", "г. Минск", 36)
    officer2.show()
    print("\n")
