#include "student.h"

Student::Student() {}
Student::Student(string name) {
    this->name = name;
}
Student::Student(const Student &other) {
    name = other.name;
}
Student::~Student() {}

bool Student::operator == (const Student &right) {
    return name == right.name;
}
bool Student::operator != (const Student &right) {
    return !(*this == right);
}
Student &Student::operator = (const Student &right) {
    name = right.name;
    return *this;
}

void Student::Print() {
    cout << endl << "Name of student: " << name << endl;
}
void Student::Read() {
    cout << endl << "Enter the name of student: ";
    cin >> name;
}