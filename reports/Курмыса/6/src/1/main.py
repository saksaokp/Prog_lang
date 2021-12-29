class Flat:
  count = 0 # количество созданных объектов класса

  __address = str() # адрес квартиры
  __area = int() # площадь квартиры
  __floor = int() # этаж

  # конструктор без параметров (по умолчанию)
  # рекомендуется объявлять лишь один конструктор в классе + можно сразу подставлять значения по умолчанию
  # def __init__(self):
  #   self.count += 1
  #   print('Создан новый объект. Количество созданных объектов:', self.count)
  
  def __init__(self, address = "", area = 0, floor = 0): # конструктор с параметрами; если их нет, то ставятся по умолчанию
    try:
      Flat.count += 1
      print('\nСоздан новый объект. Количество созданных объектов:', self.count, end='\n\n')
      self.__address = address
      self.__area = int(area)
      self.__floor = int(floor)
    except ValueError as e:
      print(e)
  
  def get_address(self):
    return self.__address
  
  def get_area(self):
    return self.__area
  
  def get_floor(self):
    return self.__floor
  
  def set_address(self, address):
    self.__address = address
  
  def set_area(self, area):
    self.__area = area
  
  def set_floor(self, floor):
    self.__floor = floor
  
  def read(self):
    try:
      self.__address= input('Введите адрес квартиры: ')
      self.__area = int(input('Введите площадь квартиры (в кв. м): '))
      self.__floor = input('Введите номер этажа, на котором расположена квартира: ')
    except ValueError as e:
      print(e)
  
  def show(self):
    print('\n' + '-' * 20)
    print('Адрес:', self.__address, '\nПлощадь:', self.__area, 'кв. м\nНомер этажа:', self.__floor)
    print('-' * 20)

if __name__ == "__main__":
  grad1 = Flat() # вызов конструктора по умолчанию 
  grad1.read() # запись данных в объект через функцию
  grad1.show() # вывод данных в консоль

  grad2 = Flat("Москва, ул. Останкинская, д. 14, кв. 81", 129, 9) # вызов конструктора с параметрами
  print('Адрес 2-ой квартиры:', grad2.get_address())
  print('Номер этажа 2-ой квартиры:', grad2.get_floor()) # получение данных при помощи геттеров

  grad3 = Flat() # вызов конструктора по умолчанию
  grad3.set_address("Санкт-Петербург, ул. Шуховская, д. 42, кв. 69")
  grad3.set_floor(4) # запись данных при помощи сеттеров
  print('Площадь 3-ей квартиры:', grad3.get_area()) # мы не записывали площадь в геттерах, но по умолчанию она равна 0, так что ошибки не будет
  grad3.show()
