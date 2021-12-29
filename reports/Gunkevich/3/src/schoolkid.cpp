#include "schoolkid.h"

Schoolkid::Schoolkid() {}
Schoolkid::Schoolkid(string name, int age) {
    this->name = name;
    this->age = age;
}
Schoolkid::Schoolkid(const Schoolkid &other) {
    name = other.name;
    age = other.age;
}
Schoolkid::~Schoolkid() {}

bool Schoolkid::operator == (const Schoolkid &right) {
    return age == right.age;
}
bool Schoolkid::operator != (const Schoolkid &right) {
    return !(*this == right);
}
Schoolkid &Schoolkid::operator = (const Schoolkid &right) {
    age = right.age;
    return *this;
}

void Schoolkid::Print() {
    cout << endl << "Name of schoolkid: " << name << endl;
    cout << endl << "Age of schoolkid: " << age << endl;
}
void Schoolkid::Read() {
    cout << endl << "Enter the name of schoolkid: ";
    cin >> name;
    cout << endl << "Enter the age of schoolkid: ";
    cin >> age;
}

