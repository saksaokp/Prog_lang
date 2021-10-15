class HRDepatrment:
	count = 0
	__employees = list()

	def __init__(self, employees=[]):
		HRDepatrment.count += 1
		print('Count:', HRDepatrment.count)

		self.__employees = employees

	def __del__(self):
		HRDepatrment.count -= 1
		print('Disposed 1 object')

	def get_employees(self):
		return self.__employees

	def set_employees(self, employees):
		if len(employees) > 0:
			self.__employees = employees
		else:
			print('Invalid argument')

	def clear_employees_list(self):
		self.__employees = []


# Usage
if __name__ == '__main__':
	first = HRDepatrment()
	last = HRDepatrment(['Olga', 'George'])

	print(last.get_employees())

	first.set_employees(['Bess', 'Tom'])
	print(first.get_employees())

	first.clear_employees_list()
	last.clear_employees_list()
	