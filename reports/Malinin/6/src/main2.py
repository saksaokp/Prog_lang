class Man:
    count = 0
    name = str()
    year = int()
    ves = int()

    def __init__(self):
        Man.count += 1

    def __init__(self, name="", year=0, ves=0):
        Man.count += 1
        self.name = name
        self.year = year
        self.ves = ves

    def __del__(self):
        print("Удаление объекта класса Man номер ", self.count)
        Man.count -= 1

    def set_name(self, nm):
        self.name = nm

    def set_year(self, ye):
        self.year = ye

    def set_ves(self, vs):
        self.ves = vs

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_ves(self):
        return self.ves

    def read(self):
        self.name = str(input("Введите имя: "))
        self.year = int(input("Введите датy рождения:"))
        self.ves = int(input("Введите вес:"))

    def show(self):
        print(" Имя: " + self.name + " Дата рождения: " + str(self.year) + " Вес: " + str(self.ves))


class Prodavec(Man):
    stag = int()
    zrp = int()

    def __init__(self,name="", year=0, ves=0,stag=0,zrp=0):
        Man.count += 1
        self.name = name
        self.year = year
        self.ves = ves
        self.stag = stag
        self.zrp = zrp

    def __del__(self):
        print("Удаление объекта класса Prod номер ", self.count)
        Man.count -= 1

    def set_stag(self, sg):
        self.stag = sg

    def set_zrp(self, zp):
        self.zrp = zp

    def get_zrp(self):
        return self.zrp

    def get_stag(self):
        return self.stag

    def read(self):
        self.name = str(input("Введите имя: "))
        self.year = int(input("Введите датy рождения:"))
        self.ves = str(input("Введите вес:"))
        self.stag = int(input("Введите стаж:"))
        self.zrp = int(input("Ввведите зарплату:"))

    def show(self):
        print("Имя: " + self.name + " Дата рождения: " + str(self.year) + " Вес: " + str(self.ves) + " Стаж " + str(self.stag) + " Зарплата " + str(self.zrp))

class Shofer(Prodavec):


    def __init__(self, name="", year=0, ves=0, stag=0, zrp=0):
        Man.count += 1
        self.name = name
        self.year = year
        self.ves = ves
        self.stag = stag
        self.zrp = zrp

    def __del__(self):
        print("Удаление объекта класса Shofer номер ", self.count)
        Man.count -= 1

    def set_stag(self, sg):
        self.stag = sg

    def set_zrp(self, zp):
        self.zrp = zp

    def get_zrp(self):
        return self.zrp

    def get_stag(self):
        return self.stag

    def read(self):
        self.name = str(input("Введите имя: "))
        self.year = int(input("Введите датy рождения:"))
        self.ves = str(input("Введите вес:"))
        self.stag = int(input("Введите стаж:"))
        self.zrp = int(input("Ввведите зарплату:"))

    def show(self):
        print("Имя: " + self.name + " Дата рождения: " + str(self.year) + " Вес: " + str(self.ves) + " Стаж " + str(
            self.stag) + " Зарплата " + str(self.zrp))

man = Man("Oleg",1,2)
man.show()
Prodavec = Prodavec("Glib",3,5,1,1)
Prodavec.show()
Shofer=Shofer("Andru",1,1,1,1)
Shofer.show()
