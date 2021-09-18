# Вариант 9 Задание 1-18
# Автобус
class Bus:
    counter = 0
    __name: str
    __speed: int
    __passengers: int

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

    def __init__(self, name: str = 'nameless', speed: int = 0, passengers: int = 0) -> None:
        Bus.counter += 1
        self.__name = name
        self.__speed = speed
        self.__passengers = passengers

    def __str__(self) -> str:
        return f'Bus (name: {self.__name}, speed: {self.__speed}, ' \
               f'passengers: {self.passengers}; counter: {Bus.counter})'

    def print(self) -> None:
        print(self)


print('Задание 1')
maz = Bus('maz', 120)
maz.print()
mercedes = Bus('mercedes', 150)
mercedes.print()


# Вариант 9 Задание 2-13:
# Актер-Сотрудник-Режиссер
class Employee:
    _name: str
    _age: int
    _salary: int

    def __init__(self, name='nameless', age=0, salary=0):
        self._name = name
        self._age = age
        self._salary = salary

    def __str__(self):
        return f'Employee: {self._name}, {self._age}, {self._salary}'

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

    def __init__(self, name, age, salary, role):
        super().__init__(name, age, salary)
        self._role = role

    def __str__(self):
        prev = super().__str__()
        return 'Actor' + prev[prev.find(':'):] + f', {self._role}'

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role


class Director(Actor):
    _film: str

    def __init__(self, name, age, salary, role, film):
        super().__init__(name, age, salary, role)
        self._film = film

    def __str__(self):
        prev = super().__str__()
        return 'Director' + prev[prev.find(':'):] + f', {self._film}'

    @property
    def film(self):
        return self._film

    @film.setter
    def film(self, film):
        self._film = film


print('Задание 2')
employee = Employee('Random woman', 60, 600)
actor = Actor('Kirill', 18, 1500, 'main')
director = Director('Michel', 19, 3600, 'director', 'The last choice')
people = [employee, actor, director]
print(*people, sep='\n', end='\n\n')

employee.name = 'Lida'
actor.role = 'second'
actor.salary = 1200
director.film = 'The last chance'
director.role = 'BigBoss'
director.salary += 1000

print(*people, sep='\n')
