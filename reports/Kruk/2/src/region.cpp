#include "region.h"

region::region() {
    name = new char[100];
    square = 0;
    populations = 0;
    next = nullptr;
}

region::region(region &copy) {
    name = copy.name;
    square = copy.square;
    populations = copy.populations;
    next = nullptr;
}

region::region(char *new_name, float new_square, int new_populations) {
    name = new_name;
    square = new_square;
    populations = new_populations;
    next = nullptr;
    Add();
}

region::~region() noexcept {
    delete[] name;
}

void region::Add() {
    if (head == nullptr || head == this)
        head = this;
    else {
        region *counter = head;
        while (counter->next && counter->next != this)
            counter = counter->next;
        counter->next = this;
    }
}

void region::Show() {
    region *counter = head;
    while (counter) {
        cout << "Название: " << counter->name << endl << "Площадь области: " << counter->square << endl
             << "Население: " << counter->populations
             << endl;
        counter = counter->next;
    }
    this->next = nullptr;
}

void region::Show_list() {
    region *counter = head;
    while (counter) {
        cout << "Название: " << counter->name << endl << "Площадь области: " << counter->square << endl
             << "Население: " << counter->populations
             << endl << endl;
        counter = counter->next;
    }
}