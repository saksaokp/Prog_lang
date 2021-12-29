#include "Foursquare.h"

Foursquare::Foursquare() {
    cout << "Введите сторону: ";
    cin >> a;
}

Foursquare::Foursquare(double a) {
    this->a = a;
}

double Foursquare::square() {
    return a * a;
}

double Foursquare::perimeter() {
    return 4 * a;
}

void Foursquare::print() {
    cout << "Квадрат: " << endl
    << "Сторона: " << a << endl;
}

bool Foursquare::operator==(const Foursquare &foursquare) {
    return (a == foursquare.a);
}

bool Foursquare::operator!=(const Foursquare &foursquare) {
    return (a != foursquare.a);
}

Foursquare &Foursquare::operator=(const Foursquare &foursquare) {
    a = foursquare.a;
    return *this;
}

Foursquare::~Foursquare() {
    a = 0;
}