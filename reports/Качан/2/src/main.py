#Задание 1.
print('Task 1:')
import os.path
path = "D:\pythonlabs\pythonProject"
num_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])
print('Number of files: ',num_files)

#Задание 2:
print('Task 2:')
import csv
list_ = []
with open("1.csv", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    head = 0
    _list = []
    for row in reader:
        if head == 0:
            print(f'{row[0]} {row[1]:<28} {row[2]:<15} {row[3]}')
        else:
            _list.append(row)
            print(f'{row[0]} {row[1]:<28} {row[2]:<15} {row[3]}')

        head = 1
    print("Changed ages: ")
    head = 0
    for row_ in _list:
        row_[2] = str(int(row_[2]) - 1)
        if head == 0:
            print(f'{row_[0]} {row_[1]:<28} {row_[2]:<15} {row_[3]}')
        else:
            print(f'{row_[0]} {row_[1]:<28} {row_[2]:<15} {row_[3]}')
        head = 1
    print(_list)
    with open("2.csv", mode="w", encoding="utf-8") as wfile:
        s = csv.writer(wfile,lineterminator='\r' )
        s.writerow(['№','ФИО','Возраст','Группа'])
        for i in _list:
            s.writerow(i)

