#include "Factory.h"

Factory::Factory(string name, int number, string position): Sudos(name, number) {
    this->position = position;
}

void Factory::show() {
    cout << "Name of organization: " <<this->name << endl << "Number of ships: " << this->number << endl << "Position: " <<this->position <<endl;
}

void Factory::set_position(string position) {
    this->position = position;
}

string Factory::get_position(){
    return this->position;
}
