from student import Student

class Undergrad(Student):
  count = 0
  __undergrad_number = 0
  _project_theme = str() # тема проекта
  _director = str() # научный руководитель

  def __init__(self, name='Магистрант', age=0, town='Город_магистрант', course=0, specialty='Специальность_магистрант', university='Университет_магистрант', project_theme='Темапроекта_магистрант', director='Научрук_магистрант'):
    Undergrad.count += 1
    self.__undergrad_number = Undergrad.count
    print('Вызов конструктора класса Undergrad No.', self.__undergrad_number)
    super(Undergrad, self).__init__(name, age, town, course, specialty, university)
    self._project_theme = project_theme
    self._director = director
  
  def __del__(self):
    print('Удаляется объект класса Undergrad No.', self.__undergrad_number)
    super().__del__()
  
  def get_project_theme(self):
    return self._project_theme
  
  def get_director(self):
    return self._director 
  
  def set_project_theme(self, project_theme):
    self._project_theme = project_theme
  
  def set_director(self, director):
    self._director = director
  
  def read(self):
    try:
      self._name = input('Введите имя магистранта: ')
      self._age = int(input('Введите возраст магистранта: '))
      self._town = input('Введите город магистранта: ')
      self._course = int(input('Введите курс магистранта: '))
      self._specialty = input('Введите специальность магистранта: ')
      self._university = input('Введите университет магистранта: ')
      self._project_theme = input('Введите тему научного проекта: ')
      self._director = input('Введите ФИО начуного руководителя: ')
    except ValueError as e:
      print(e)
  
  def show(self):
    print(
      'Имя:', self._name, 
      '\nВозраст:', self._age,
       '\nГород:', self._town, 
       '\nКурс:', self._course,
        '\nСпециальность:', self._specialty,
         '\nУниверситет:', self._university, 
         '\nТема проекта:', self._project_theme,
          '\nФИО научного руководителя:', self._director, end='\n\n')
