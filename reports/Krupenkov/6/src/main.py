# Вариант 9 Задание 1-18
# Автобус
class Bus:
    counter = 0
    __name: str
    __speed: int
    __passengers: int

    def __init__(self, name: str = 'nameless', speed: int = 0, passengers: int = 0):
        Bus.counter += 1
        self.__name = name
        self.__speed = speed
        self.__passengers = passengers
        print(f'Created {self}')

    def __str__(self) -> str:
        return f'Bus (name: {self.__name}, speed: {self.__speed}, ' \
               f'passengers: {self.passengers}; counter: {Bus.counter})'

    def __del__(self):
        print(f'Deleted {self}')

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int) -> None:
        self.__speed = speed

    @property
    def passengers(self) -> int:
        return self.__passengers

    @passengers.setter
    def passengers(self, passengers: int) -> None:
        self.__passengers = passengers


# Вариант 9 Задание 2-13:
# Актер<-Сотрудник->Режиссер
class Employee:
    _name: str
    _age: int
    _salary: int

    def __init__(self, name='nameless', age=0, salary=0):
        self._name = name
        self._age = age
        self._salary = salary
        print(f'Created employee: {self._name}, {self._age}, {self._salary}')

    def __str__(self) -> str:
        return f'Employee: {self._name}, {self._age}, {self._salary}'

    def __del__(self):
        print(f'Deleted {self}')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary


class Actor(Employee):
    _role: str

    def __init__(self, name='nameless', age=0, salary=0, role='empty'):
        super().__init__(name, age, salary)
        self._role = role
        prev: str = super().__str__()
        print(f'Created actor{prev[prev.find(":"):]}, {self._role}')

    def __str__(self):
        prev: str = super().__str__()
        return 'Actor' + prev[prev.find(':'):] + f', {self._role}'

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role


class Director(Employee):
    _film: str

    def __init__(self, name='nameless', age=0, salary=0, film='secret'):
        super().__init__(name, age, salary)
        self._film = film
        prev: str = super().__str__()
        print(f'Created director{prev[prev.find(":"):]}, {self._film}')

    def __str__(self):
        prev: str = super().__str__()
        return 'Director' + prev[prev.find(':'):] + f', {self._film}'

    @property
    def film(self):
        return self._film

    @film.setter
    def film(self, film):
        self._film = film


def main():
    print('Задание 1')
    maz = Bus('maz', 120, 50)
    mercedes = Bus('mercedes', 150, 35)
    maz.passengers = 55
    mercedes.speed = 140
    print(maz)
    print(mercedes)

    print('\nЗадание 2')
    print('Создание экземпляров класса:')
    employee = Employee('Random woman', 60, 600)
    actor = Actor('Kirill', 18, 1500, 'main')
    director = Director('Michel', 19, 3600, 'The last choice')
    people = [employee, actor, director]

    employee.name = 'Lida'
    actor.role = 'second'
    actor.salary = 1200
    director.film = 'The last chance'
    director.salary += 1000

    print('Изменение:', *people, sep='\n')
    print('Сборщик мусора:')


if __name__ == '__main__':
    main()
