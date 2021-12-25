#include "class.h"

Product::Product() {
    name = "-";
    number = 0;
    price = 0;
    cout << "Конструктор без параметров вызван для объкта " << this << endl;
}

Product::Product(char *NAME, const int NUMBER, const float PRICE) {
    name = NAME;
    number = NUMBER;
    price = PRICE;
    cout << "Конструктор с параметрами вызван для объкта " << this << endl;
}

Product::Product(const Product &Copy) {
    name = Copy.name;
    number = Copy.number;
    price = Copy.price;
    cout << "Конструктор копированния вызван для объкта " << this << endl;
}

Product::~Product() {
    delete name;
    delete &number;
    delete &price;
    cout << "Деструктор был вызван для объекта " << this << endl;
}

char *Product::GatName() {
    return name;
}

int Product::GetNumber() {
    return number;
}

float Product::GetPrice() {
    return price;
}

void Product::Show() {
    cout << "Название: " << name << endl
         << "Количество: " << number << endl
         << "Цена: " << price << " руб." << endl << endl;
}

void Product::SetName(char *new_name) {
    name = new_name;
}

void Product::SetNumber(int new_number) {
    number = new_number;
}

void Product::SetPrice(float new_price) {
    price = new_price;
}

void Product::Set(char *new_name, int new_number, float new_price) {
    name = new_name;
    number = new_number;
    price = new_price;
}