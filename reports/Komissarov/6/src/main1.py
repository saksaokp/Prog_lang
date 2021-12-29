class Bank:
    counter = 0
    __name: str
    __money: int
    __workers: int

    def __init__(self, name: str = 'без параметра', money: int = 0, workers: int = 0) -> None:
        Bank.counter += 1
        self.__name = name
        self.__money = money
        self.__workers = workers
        print(f'Создан {self}')



    def __str__(self) -> str:
        return f'Банк (name: {self.__name}, капитал: ${self.__money}, ' \
               f'рабочие: {self.workers}; счётчик: {Bank.counter})'

    def __del__(self) -> None: #деструктор
        print(f'Удалён банк "{self.__name}"')

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def money(self) -> int:
        return self.__money

    @money.setter
    def money(self, money: int) -> None:
        self.__money = money

    @property
    def workers(self) -> int:
        return self.__workers

    @workers.setter
    def workers(self, workers: int) -> None:
        self.__workers = workers

    def in_name(self):
        self.__name = input('name: ')
    def in_money(self):
        self.__money = input('money: ')
    def in_workers(self):
        self.__workers = input('workers: ')


defaultBank=Bank()
specialBank=Bank('Банк Golden Coast NY', 300000, 21)

print(defaultBank)
print(specialBank)

specialBank.in_name()
print(specialBank)