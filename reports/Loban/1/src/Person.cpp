#include <iostream>
#include "Person.h"

using namespace std;

Person::Person() {
    name = "DiCaprio";
    age = 46;
    isMale = true;
    cout << name << " was created, Constructor()" << endl;
}

Person::Person(const char *name2, int age2, bool isMale2) {
    name = name2;
    age = age2;
    isMale = isMale2;
    cout << name << " was created, Constructor(values)" << endl;
}

Person::Person(Person &person) {
    name = person.name;
    age = person.age;
    isMale = person.isMale;
    cout << name << " was created, Constructor(&link);" << endl;
}

Person::~Person() {
    cout << name << " was deleted" << endl;
}

void Person::Print() {
    cout << name << endl;
    cout << "Age: " << age << endl;
    cout << "Sex: ";
    if (isMale){
        cout << "male";
    } else {
        cout << "female";
    }
    cout << endl;
}

void Person::SetName(const char *name2) {
    name = name2;
}

const char *Person::GetName() {
    return name;
}

void Person::SetAge(int age2) {
    age = age2;
}

int Person::GetAge() {
    return age;
}

void Person::SetSex(bool isMale2) {
    isMale = isMale2;
}

bool Person::GetSex() {
    return isMale;
}
