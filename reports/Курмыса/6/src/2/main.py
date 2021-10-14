from pupil import Pupil
from student import Student
from undergrad import Undergrad

if __name__ == "__main__":
  person1 = Pupil()
  person1.read()
  print('Данные по первому учащемуся:')
  person1.show()
  person2 = Pupil('Егор', 13, 'Кобрин')
  print('Имя второго учащегося:', person2.get_name())
  print('Город второго учащегося:', person2.get_town())

  person3 = Student()
  person4 = Student('Артём', 18, 'Брест')
  person3.read()
  person4.set_specialty('ИИ')
  person4.set_course(1)
  person4.set_university('БрГУ им. Пушкина')
  print('Данные по третьему учащемуся:')
  person3.show()
  print('Данные по четвёртому учащемуся:')
  person4.show()

  person5 = Undergrad()
  print('Данные по пятому учащемуся (дефолтные):')
  person5.show()
  person5.read()
  print('Тема научного проекта для пятого учащегося:', person5.get_project_theme())
  print('ФИО научного руководителя пятого учащегося:', person5.get_director())
  print('Данные по пятому учащемуся (введённые):')
  person5.show()

  del person1, person2, person3, person4, person5
