from typing import List, Optional


def reading():
    with open('files/students.csv', 'r', encoding='utf-8') as file:
        students: List[List[Optional[str, int]]] = []
        for line in file.read().split('\n'):
            students.append(line.split(';'))
    header = students.pop(0)
    for student in students:
        student[0] = int(student[0])
        student[2] = int(student[2])
    students.sort(key=lambda x: x[1])
    return header, students


def decrease(students):
    for student in students:
        student[2] -= 1
    # print(students)


def save(header, students):
    to_save: str = ''
    row_sep = ''
    for student in [header] + students:
        to_save += row_sep
        row_sep = '\n'
        val_sep = ''
        for i in student:
            to_save += val_sep + str(i)
            val_sep = ';'
    with open('files/new_students.csv', 'w', encoding='utf-8') as file:
        file.write(to_save)

def main():

    header, students = reading()
    decrease(students)
    save(header, students)


if __name__ == '__main__':
    main()