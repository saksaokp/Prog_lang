class Pupil:
  count = 0
  __pupil_number = int()
  _name = str()
  _age = int()
  _town = str()

  def __init__(self, name='Учащийся', age=0, town='Город_учащийся'):
    Pupil.count += 1
    self.__pupil_number = Pupil.count
    print('Вызов конструктора класса Pupil No.', self.__pupil_number)
    self._name = name
    self._age = int(age)
    self._town = town
  
  def __del__(self):
    print('Удаляется объект класса Pupil No.', self.__pupil_number)
  
  def get_name(self):
    return self._name
  
  def get_age(self):
    return self._age
  
  def get_town(self):
    return self._town
  
  def set_name(self, name):
    self._name = name
  
  def set_age(self, age):
    self._age = age
  
  def set_town(self, town):
    self._town = town

  def read(self):
    try:
      self._name = input('Введите имя учащегося: ')
      self._age = int(input('Введите возраст учащегося: '))
      self._town = input('Введите город учащегося: ')
    except ValueError as e:
      print(e)
  
  def show(self):
    print('Имя:', self._name, '\nВозраст:', self._age, '\nГород:', self._town, end='\n\n')
