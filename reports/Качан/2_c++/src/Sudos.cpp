#include "Sudos.h"

Sudos::Sudos(string name, int number): Organization(name) {
    this->number = number;
}

void Sudos::show() {
    cout << "Organization name: " << this->name << endl << "Number of ships: " << this->number << endl;
}

void Sudos::set_number(int number) {
    this->number = number;
}

int Sudos::get_number() {
    return this->number;
}
