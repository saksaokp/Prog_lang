#include <iostream>
#include "Person.h"

using namespace std;

int main() {
    Person *diCampio = new Person;
    diCampio->Print();
    Person *keanu = new Person("Keanu", 57, true);
    keanu->Print();
    Person *salma1 = new Person("Salma", 55, false);
    Person *salma = new Person(*salma1);
    salma->Print();
    cout << endl;

    diCampio->SetName("Kirillio");
    cout << diCampio->GetName() << endl;
    keanu->SetAge(100);
    cout << keanu->GetAge() << endl;
    salma->SetSex(true);
    cout << salma->GetSex() << endl;
    cout << endl;

    void (Person::*ptr)();
    ptr = &Person::Print;

    diCampio->Print();
    keanu->Print();
    salma->Print();

    delete diCampio;
    delete keanu;
    delete salma;
}
