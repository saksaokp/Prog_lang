#Задание 1
class hospital:
    __counter = 0
    __name = str()
    __salary = int()
    __work = int()

    def __init__(self, name = '', salary = 0, workers = 0):
        hospital.__counter += 1
        self.__name = name
        self.__salary = salary
        self.__work = workers

    # def __del__(self):
    #     hospital.__counter -= 1
    #     print(f'Destructor for {self.__name}')

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_workers(self):
        return self.__work

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def set_workers(self, workers):
        self.__work = workers

    def show(self):
        print(f'Name: {self.__name}, Salary: {self.__salary}, Number of workers: {self.__salary}, counter: {self.__counter}')


hsp1 = hospital(input('Enter name: '), input('Enter salary: '), input('Enter number of workers: '))
hsp1.show()

#Задание 2:
class person:
    counter = 0
    __age = int()
    __height = int()
    __name = str()

    def __init__(self, age = 0, height = 0, name = ''):
        person.counter += 1
        self.__age = age
        self.__height = height
        self.__name = name

    def __del__(self):
        print('Вызов деструктора: '+str(person.counter))
        person.counter -= 1

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def set_height(self, height):
        self.__height = height

    def set_name(self, name):
        self.__name = name

    def show(self):
        print(f'Age: {self.__age}, Height: {self.__height}, Name: {self.__name}')



class Military(person):
    __rank = str()
    __num = int()

    def __init__(self, age = 0, height = 0, name = '', rank = '', num = 0):
        super().__init__(age, height, name)
        self.__rank = rank
        self.__num = num

    def get_rank(self):
        return self.__rank

    def get_num(self):
        return self.__num

    def set_rank(self, rank):
        self.__rank = rank

    def set_num(self, num):
        self.__num = num

    def show(self):
        print(f'Age: {self.get_age()}, Height: {self.get_height()}, Name: {self.get_name()}, Rank: {self.__rank}, Squad number: {self.__num}')



class recruit(Military):
    __date = str()
    def __init__(self, age = 0, height = 0, name = '', rank = '', num = 0, date = ''):
        super().__init__(age, height, name, rank, num)
        self.__date = date


    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def show(self):
        print(f'Age: {self.get_age()}, Height: {self.get_height()}, Name: {self.get_name()}, Rank: {self.get_rank()}, Squad number: {self.get_num()}, Date of call: {self.__date}')

p1 = person(int(input('Enter age: ')), int(input('Enter height: ')), input('Enter name: '))
p1.show()
p2 = Military(int(input('Enter age: ')), int(input('Enter height: ')), input('Enter name: '), input('Enter rank: '), int(input('Enter squad number: ')))
p2.show()
p3 = recruit(int(input('Enter age: ')), int(input('Enter height: ')), input('Enter name: '), input('Enter rank: '), int(input('Enter squad number: ')), input('Enter date: '))
p3.show()
