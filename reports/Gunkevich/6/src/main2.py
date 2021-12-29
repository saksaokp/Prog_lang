class Teacher:
    subject = str()

    def __init__(self):
        print("Вызван конструктор без параметров Teacher", self)

    def __init__(self, sb=""):
        print("Конструтор класса Teacher с параметрами вызван", self)
        try:
            self.subject = sb
        except ValueError:
            print("Ошибка ввода")

    def set_subject(self, sb):
        self.subject = sb

    def get_subject(self):
        return self.subject

    def __del__(self):
        print("Вызван деструктор класса Teacher", self)

    def read(self):
        try:
            self.subject = str(input("Введите название предмета, которым обучает учитель:\n"))
        except ValueError:
            print("Ошибка ввода")

    def show(self):
        print("Специальность учителя:", self.subject)


class Persona(Teacher):
    name = str()

    def __init__(self):
        print("Вызван конструктор без параметров класса Persona", self)

    def __init__(self, nm="", sb=""):
        print("Вызван конструктор класса Persona с параметрами", self)
        try:
            self.name = nm
            self.subject = sb
        except ValueError:
            print("Ошибка ввода")

    def set_name(self, nm):
        self.name = nm

    def get_name(self):
        return self.name

    def __del__(self):
        print("Вызван деструктор класса Persona", self)

    def read(self):
        try:
            self.name = input("Введите имя учителя:\n")
            self.subject = input("Введите название прдмета:\n")
        except ValueError:
            print("Ошибка ввода")

    def show(self):
        print("Специальность учителя: ", self.subject)
        print("Имя учителя: ", self.name)


class Schoolkid(Persona):
    fio = str()

    def __init__(self):
        print("Вызван конструктор класса Schoolkid без параметров", self)

    def __init__(self, nm="", sb="", fi=""):
        print("Вызван конструктор с параметрами для класса Schoolkid", self)
        try:
            self.name = nm
            self.subject = sb
            self.fio = fi
        except ValueError:
            print("Ошибка ввода")

    def __del__(self):
        print("Вызван деструктор класса Schoolkid", self)

    def set_fi(self, fi):
        self.fio = fi

    def get_fi(self):
        return self.fio

    def read(self):
        try:
            self.name = input("Введите имя учителя:\n")
            self.subject = input("Введите название прдмета:\n")
            self.fio = input("Введите фамилию и имя ученика:\n")
        except ValueError:
            print("Ошибка ввода")

    def show(self):
        print("Специальность учителя: ", self.subject)
        print("Имя учителя: ", self.name)
        print("Фамилия и имя ученика:", self.fio)


if __name__ == '__main__':
    teacher1 = Teacher()
    teacher1.set_subject("Физика")
    teacher1.show()
    teacher2 = Teacher("История")
    teacher2.show()
    person1 = Persona()
    person1.read()
    person1.show()
    person2 = Persona("Валера", "Математика")
    person2.show()
    schoolkid1 = Schoolkid()
    schoolkid1.read()
    schoolkid1.show()
    schoolkid2 = Schoolkid("Виталик", "Английский", "Димон")
    schoolkid2.show()
