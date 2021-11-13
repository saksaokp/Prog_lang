#include "metropolis.h"

metropolis::metropolis() : town() {
    gdp = 0;
    next = nullptr;
}

metropolis::metropolis(metropolis &copy) : town(copy) {
    gdp = copy.gdp;
    *this = copy;
    next = nullptr;
}

metropolis::metropolis(char *new_name, float new_square, int new_populations, int new_year, float new_gdp) : town(
        new_name, new_square, new_populations, new_year) {
    gdp = new_gdp;
    next = nullptr;
    Add();
}

metropolis::~metropolis() noexcept {
    delete[] name;
}

void metropolis::Add() {
    if (head == nullptr || head == this)
        head = this;
    else {
        metropolis *counter = head;
        while (counter->next && counter->next != this)
            counter = counter->next;
        counter->next = this;
    }
}

void metropolis::Show() {
    metropolis *counter = head;
    while (counter) {
        cout << "Название: " << counter->name << endl << "Площадь области: " << counter->square << endl
             << "Населенние: " << counter->populations << endl << "Год основания: " << counter->year << endl
             << "ВВП: " << counter->gdp << endl << endl;
        counter = counter->next;
    }
}

void metropolis::Show_list() {
    metropolis *counter = head;
    while (counter) {
        cout << "Название: " << counter->name << endl << "Площадь области: " << counter->square << endl
             << "Населенние: " << counter->populations << endl << "ВВП: " << counter->gdp << endl << endl;
        counter = counter->next;
    }
}

void metropolis::setGdp(float gdp) {
    metropolis::gdp = gdp;
}
