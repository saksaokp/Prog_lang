#include "preschooler.h"

Preschooler::Preschooler() {}
Preschooler::Preschooler(string name, int age) {
    this->name = name;
    this->age = age;
}
Preschooler::Preschooler(const Preschooler &other) {
    name = other.name;
    age = other.age;
}
Preschooler::~Preschooler() {}

bool Preschooler::operator == (const Preschooler &right) {
    return age == right.age;
}
bool Preschooler::operator != (const Preschooler &right) {
    return !(*this == right);
}
Preschooler &Preschooler::operator = (const Preschooler &right) {
    age = right.age;
    return *this;
}

void Preschooler::Print() {
    cout << endl << "Name of preschooler: " << name << endl;
    cout << endl << "Age of preschooler: " << age << endl;
}
void Preschooler::Read() {
    cout << endl << "Enter the name of preschooler: ";
    cin >> name;
    cout << endl << "Enter the age of preschooler: ";
    cin >> age;
}