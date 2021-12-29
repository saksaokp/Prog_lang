#include "town.h"

town::town() : place() {
    year = 0;
    next = nullptr;
}

town::town(town &copy) : place(copy) {
    year = copy.year;
    next = nullptr;
}

town::town(char *new_name, float new_square, int new_populations, int new_year) :
        place(new_name, new_square, new_populations) {
    year = new_year;
    next = nullptr;
}

town::~town() noexcept {
    delete[] name;
}

void town::Add() {
    if (head == nullptr || head == this)
        head = this;
    else {
        town *counter = head;
        while (counter->next && counter->next != this)
            counter = counter->next;
        counter->next = this;
    }
}

void town::Show() {
    town *counter = head;
    while (counter) {
        cout << "Название: " << counter->name << endl << "Площадь области: " << counter->square << endl
             << "Населенние: " << counter->populations << endl << "Год основания: " << year << endl << endl;
        counter = counter->next;
    }
}

void town::Show_list() {
    town *counter = head;
    while (counter) {
        cout << "Название: " << counter->name << endl << "Площадь области: " << counter->square << endl
             << "Населенние: " << counter->populations << endl << "Год основания: " << counter->year << endl << endl;
        counter = counter->next;
    }
}

void town::setYear(int year) {
    town::year = year;
}
