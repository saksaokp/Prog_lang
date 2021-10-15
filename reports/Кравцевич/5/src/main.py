import os
import csv

target_file = 'students.csv'
default_dict = 'D:\\'
current_data = []


def count_files():
	folder_path = input('Write path: ')
	if not os.path.isdir(folder_path):
		print('Not directory')
		return
	output = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
	print('Files:')
	print(*output, sep='\n')
	print('Files count: ', len(output))
	return output


def read_csv(file_name=target_file):
	with open(file_name, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')

		output = [row for row in reader]
		return output


def sort_by_group_number(data):
	output = [data[0]] + sorted(data[1:], key=lambda x: int(x))
	return output


def display_data(data):
	for row in data:
		print(*row, sep='\t')


def decrease_age(group):
	global current_data

	for row in current_data[1:]:
		if row[-1] == group:
			row[-2] = str(int(row[-2]) - 1)

	print('Result:')
	display_data(current_data)

	if input('Save?\n(Y)es\t(N)o\n')[0].lower() == 'y':
		save_changes(current_data)

	return current_data


def save_changes(data, file=target_file):
	with open(file, 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f, delimiter=';')
		writer.writerows(data)
	print('Saved!')


def sort_csv_file():
	global current_data
	file_name = input('Write file name: ')
	current_data = read_csv(file_name)
	current_data = sort_by_group_number(current_data)
	print('Done')


def decrease_group_age():
	group = input('Write target group')
	decrease_age(group)
	print('Done!')


def read_target_file():
	global current_data
	file_name = input('File name: ')
	current_data = read_csv(file_name)
	print('Done!')


def save_as():
	file_name = input('Write file name: ')
	save_changes(current_data, file_name)
	print('Done!')


def display():
	display_data(current_data)


def menu():
	functions = {
		1: count_files,
		2: sort_csv_file,
		3: decrease_group_age,
		4: read_target_file,
		5: save_as,
		6: display
	}

	print('1. Count files')
	print('2. Sort csv file')
	print('3. Decrease group age')
	print('4. Read csv file')
	print('5. Save csv file as...')
	print('6. Display data')
	command = int(input('Selected: '))
	functions[command]()


def main():
	while 'Python is cool!':
		menu()


if __name__ == '__main__':
	main()
