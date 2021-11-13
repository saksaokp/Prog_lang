class Person:
	__full_name = str()
	__age = int()

	def __init__(self, full_name=None, age=0):
		print('Вызван конструктор класса Person')
		self.__full_name = full_name
		self.__age = age

	def __del__(self):
		print('Вызван деструктор класса Person')

	def set_age(self, age):
		age = int(age)
		if age < 0:
			print('Invalid argument')
			return

		self.__age = age

	def get_age(self):
		return self.__age

	def set_full_name(self, full_name):
		if len(full_name) == 0:
			print('Invalid argument')
			return

		self.__full_name = full_name

	def get_full_name(self):
		return self.__full_name

	def __str__(self):
		return f'Full name: {self.get_full_name()}\nAge: {self.get_age()}'

	def console_init(self):
		self.set_full_name(input('Full name: '))
		self.set_age(input('Age: '))


class Student(Person):
	__course = int()

	def __init__(self, full_name=None, age=0, course=1):
		print('Вызван конструктор класса Student')
		super().__init__(full_name, age)
		self.__course = course

	def __del__(self):
		print('Вызван деструктор класса Student')

	def set_course(self, course):
		if 5 < course < 1:
			print('Invalid argument')
			return

		self.__course = course

	def get_course(self):
		return self.__course

	def __str__(self):
		return f'Full name: {self.get_full_name()}\nAge: {self.get_age()}\nCourse: {self.get_course()}'

	def console_init(self):
		super(Student, self).console_init()
		self.set_course(input('Course: '))


class Teacher(Person):
	__lesson_type = str()

	def __init__(self, full_name=None, age=0, lesson_type=None):
		print('Вызван конструктор класса Teacher')
		super().__init__(full_name, age)
		self.__lesson_type = lesson_type

	def __del__(self):
		print('Вызван деструктор класса Teacher')

	def set_lesson_type(self, lesson_type):
		if len(lesson_type) == 0:
			print('Invalid argument')

		self.__lesson_type = lesson_type

	def get_lesson_type(self):
		return self.__lesson_type

	def __str__(self):
		return f'Full name: {self.get_full_name()}\nAge: {self.get_age()}\nLesson type: {self.get_lesson_type()}'

	def console_init(self):
		super(Teacher, self).console_init()
		self.set_lesson_type(input('Lesson type: '))


if __name__ == '__main__':
	person = Person('Tom', 12)
	student = Student('Bob', 18, 1)
	teacher = Teacher('Mr. Jon', 40, 'Math')

	print(str(person))
	print(str(student))
	print(str(teacher))

	teacher.console_init()
	print(teacher)