class PartyMember:
    count = 0
    __name = str()
    __party = str()
    __age = int()
    def __init__(self):
        PartyMember.count += 1
        print(PartyMember.count)

    def __init__(self, nm="", pr="", ag=0):
        PartyMember.count += 1
        print("Конструктор с параметрами вызван")
        try:
            self.__name = nm
            self.__party = pr
            self.__age = int(ag)
        except ValueError as e:
            print(e)

    def set_name(self, nm):
        self.__name = nm
    def set_party(self, pr):
        self.__party = pr
    def set_age(self, ag):
        self.__age = ag
    def get_name(self):
        return self.__name
    def get_party(self):
        return self.__party
    def get_age(self):
        return  self.__age

    def read(self):
        try:
            self.__name = str(input("Введите имя члена партии:\n"))
            self.__party = str(input("Введите название партии:\n"))
            self.__age = int(input("Введите возраст члена партии:\n"))
        except ValueError:
            print("Ошибка ввода")

    def show(self):
        print("Имя:" + self.__name + " Название партии:" + self.__party + " Возраст:" + str(self.__age))

if __name__ == "__main__":
    y = PartyMember()
    y1 = PartyMember()
    y.read()
    y1.read()
    y.show()
    y1.show()
    x = PartyMember("Михаил Пожарский", "ЦР", 47)
    x.show()
    c = PartyMember()
    c.set_name("Кто-то")
    c.set_party("Какая-то")
    c.set_age(45)
    c.show()
    print("Количество членов партий:", PartyMember.count)
