from pupil import Pupil

class Student(Pupil):
  count = 0
  __student_number = int()
  _course = int()
  _specialty = str()
  _university = str()

  def __init__(self, name='Студент', age=0, town='Город_студент', course=0, specialty='Специальность_студент', university='Университет_студент'):
    Student.count += 1
    self.__student_number = Student.count
    print('Вызов конструктора класса Student No.', self.__student_number)
    super().__init__(name, age, town)
    self._course = int(course)
    self._specialty = specialty
    self._university = university
  
  def __del__(self):
    print('Удаляется объект класса Student No.', self.__student_number)
    super().__del__()

  def get_course(self):
    return self._course
  
  def get_specialty(self):
    return self._specialty
  
  def get_university(self):
    return self._university
  
  def set_course(self, course):
    self._course = course
  
  def set_specialty(self, specialty):
    self._specialty = specialty
  
  def set_university(self, university):
    self._university = university
  
  def read(self):
    try:
      self._name = input('Введите имя студента: ')
      self._age = int(input('Введите возраст студента: '))
      self._town = input('Введите город студента: ')
      self._course = int(input('Введите курс студента: '))
      self._specialty = input('Введите специальность студента: ')
      self._university = input('Введите университет студента: ')
    except ValueError as e:
      print(e)
  
  def show(self):
    print(
      'Имя:', self._name, 
      '\nВозраст:', self._age, 
      '\nГород:', self._town, 
      '\nКурс:', self._course, 
      '\nСпециальность:', self._specialty, 
      '\nУниверситет:', self._university, end='\n\n')
