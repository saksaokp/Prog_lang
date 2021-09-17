# Вариант 9 задания 1.18, 2.13


class Bus:
    __count = 0
    __name: str
    __speed: int

    def __init__(self, name='nameless', speed=0) -> None:
        self.__count += 1
        self.__name = name
        self.__speed = speed

    def __str__(self) -> str:
        return f'Class Bus (name: {self.__name}, speed: {self.__speed})'


bus = Bus()
print(bus)

