import os
import csv

target_file = 'students.csv'
default_dict = 'D:\\'


def count_files(folder_path=default_dict):
	if not os.path.isdir(folder_path):
		print('Not directory')
		return
	output = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
	print('Files:')
	print(*output, sep='\n')
	print('Files count: ', len(output))
	return output


def read_csv(file):
	with open(file, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')

		output = [row for row in reader]
		return output


def sort_by_group_number(data):
	output = [data[0]] + sorted(data[1:], key=sort_key)
	return output


def sort_key(row):
	return int(row[0])


def display_data(data):
	for row in data:
		print(*row, sep='\t')


def decrease_age(group, file=target_file):
	data = read_csv(file)

	for row in data[1:]:
		if row[-1] == group:
			row[-2] = str(int(row[-2]) - 1)

	print('Result:')
	display_data(data)

	if input('Save?\n(Y)es\t(N)o\n')[0].lower() == 'y':
		save_changes(data)

	return data


def save_changes(data, file=target_file):
	with open(file, 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f, delimiter=';')
		writer.writerows(data)
	print('Saved!')


def main():
	print('Task 1 result: ')
	print(count_files())

	print('Task 2 result: ')
	display_data(sort_by_group_number(read_csv(target_file)))

	print('Task 3 result:')
	decrease_age('БО-1111', target_file)


if __name__ == '__main__':
	main()
