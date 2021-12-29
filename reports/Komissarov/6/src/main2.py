# Родительским классом является персона. 
# У него есть поля: имя, возраст и пол. 
# От него наследуется спортсмен с дополнительным полем вид спорта 
# и призёр c дополнительным полем занятое призовое место.
class Person:
    _name: str
    _age: int
    _sex: str

    def __init__(self, name='nameless', age=0, sex='none') -> None:
        self._name = name
        self._age = age
        self._sex = sex
        print(f'Создана персона: {self._name}, {self._age}, {self._sex}')

    def __str__(self) -> str:
        return f'Персона: {self._name}, {self._age}, {self._sex}'

    def __del__(self) -> None:
        print(f'Удалён(удалена) {self}')

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age) -> None:
        self._age = age

    @property
    def sex(self) -> str:
        return self._sex

    @sex.setter
    def sex(self, sex) -> None:
        self._sex = sex

    def in_name(self):
        self._name = input('Enter name: ')

    def in_age(self):
        self._age = input('Enter age: ')

    def in_sex(self):
        self._sex = input('Enter sex: ')


class Sportsman(Person):
    _sport: str

    def __init__(self, name='nameless', age=0, sex='none', sport='no sport') -> None:
        super().__init__(name, age, sex)
        self._sport = sport
        prev: str = super().__str__()
        print(f'Создан спортсмен {prev[prev.find(":"):]}, {self._sport}')

    def __str__(self) -> str:
        prev: str = super().__str__()
        return 'Спортсмен' + prev[prev.find(':'):] + f', {self._sport}'

    @property
    def sport(self) -> str:
        return self._sport

    @sport.setter
    def sport(self, sport) -> None:
        self._sport = sport

    def in_sport(self):
        self._sport = input('Enter sport: ')


class Prizewinner(Sportsman):
    _place: int

    def __init__(self, name='nameless', age=0, sex='none', sport='no sport', place=0) -> None:
        super().__init__(name, age, sex, sport)
        self._place = place
        prev: str = super().__str__()
        print(f'Создан призёр {prev[prev.find(":"):]}, {self._place}')

    def __str__(self) -> str:
        prev: str = super().__str__()
        return 'Призёр' + prev[prev.find(':'):] + f', {self._place}'

    @property
    def place(self) -> int:
        return self._place

    @place.setter
    def place(self, place) -> None:
        self._place = place

    def in_place(self):
        self._place = input('Enter place: ')


def main():
    print('Создание экземпляров класса:')
    person = Person('человек', 60, 'муж')
    sportsman = Sportsman('Дарья', 25, 'жен', 'лыжные гонки')
    prizewinner = Prizewinner('Виктор', 21, 'муж', 'футбол', 2)
    people = [person, sportsman, prizewinner]

    person.name = 'Анна'
    sportsman.sport = 'баскетбол'
    prizewinner.place = 1

    print('\nИзменённые экземпляры класса:', *people, sep='\n')
    print('')

    prizewinner.in_name()
    print(prizewinner)


if __name__ == '__main__':
    main()

