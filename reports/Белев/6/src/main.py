class Person:
    count = 0
    name = str()
    age = int()
    hobby = str()

    def __init__(self, name="", age=0, hobby=""):
        Person.count += 1
        self.name = name
        self.age = age
        self.hobby = hobby

    def __del__(self):
        print("Удаление объекта класса Персона номер ", self.count)
        Person.count -= 1

    def set_name(self, nm):
        self.name = nm

    def set_year(self, ae):
        self.age = ae

    def set_group(self, hy):
        self.hobby = hy

    def get_name(self):
        return self.name

    def get_year(self):
        return self.age

    def get_group(self):
        return self.hobby

    def read(self):
        self.name = str(input("\nВведите имя: "))
        self.age = int(input("Введите возраст:"))
        self.hobby = str(input("Введите хобби:"))

    def show(self):
        print("\nИмя:" + self.name + "\nВозраст: " + str(self.age) + "\nХобби: " + self.hobby)


class Sportsmen(Person):
    count = 0
    sport_type = str()
    experience = int()

    def __init__(self, name="", age=0, hobby="", sport_type="", experience=0):
        Sportsmen.count += 1
        self.name = name
        self.age = age
        self.hobby = hobby
        self.sport_type = sport_type
        self.experience = experience

    def __del__(self):
        print("Удаление объекта класса Спортсмен номер ", self.count)
        Sportsmen.count -= 1

    def set_sport_type(self, st):
        self.sport_type = st

    def set_experience(self, exp):
        self.experience = exp

    def get_sport_type(self):
        return self.sport_type

    def get_experience(self):
        return self.experience

    def read(self):
        self.name = str(input("\nВведите имя: "))
        self.age = int(input("Введите возраст:"))
        self.hobby = str(input("Введите хобби:"))
        self.sport_type = str(input("Введите вид спорта:"))
        self.experience = int(input("Введите стаж:"))

    def show(self):
        print("\nИмя:" + self.name + "\nВозраст: " + str(self.age) + "\nХобби: " + self.hobby + "\nВид спорта:" +
              self.sport_type + "\nСтаж:" + str(self.experience))


class Student(Person):
    count = 0
    age = int()
    hobby = str()

    def __init__(self, name="", age=0, group="", year=0, hobby=""):
        Student.count += 1
        self.name = name
        self.age = age
        self.hobby = hobby
        self.year = year
        self.group = group

    def __del__(self):
        print("Удаление объекта класса Студент номер ", self.count)
        Student.count -= 1

    def set_year(self, ye):
        self.year = ye

    def set_group(self, gp):
        self.group = gp

    def get_year(self):
        return self.year

    def get_group(self):
        return self.group

    def read(self):
        self.name = str(input("\nВведите имя: "))
        self.age = int(input("Введите возраст:"))
        self.hobby = str(input("Введите хобби:"))
        self.year = int(input("Введите курс:"))
        self.group = str(input("Введите группу:"))

    def show(self):
        print("\nИмя:" + self.name + "\nВозраст: " + str(self.age) + "\nХобби" + self.hobby + "\nКурс" + str(self.year) +
              "\nГруппа: " + self.group)

pers = Person("Азимов", 16, "Теннис")
pers.show()
stud = Student()
stud.read()
stud.show()
smen = Sportsmen("Волочков", 19, "Книги", "Биатлон", 3)
smen.show()