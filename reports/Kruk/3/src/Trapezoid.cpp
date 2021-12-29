#include "Trapezoid.h"

Trapezoid::Trapezoid() {
    cout << "Введите верхнее основание: ";
    cin >> bot_base;
    cout << "Введите нижнее основание: ";
    cin >> top_base;
    cout << "Введите высоту: ";
    cin >> h;
    cout << endl;
}

Trapezoid::Trapezoid(double bot_base, double top_base, double h) {
    this->bot_base = bot_base;
    this->top_base = top_base;
    this->h = h;
}

double Trapezoid::square() {
    return (bot_base + top_base) / 2 * h;
}

double Trapezoid::perimeter() {
    double side = pow((bot_base - top_base) / 2, 2) + pow(h, 2);
    return bot_base + top_base + 2 * (sqrt(side));
}

void Trapezoid::print() {
    cout << "Трапеция: " << endl
    << "Верхнее основание: " << top_base << endl
    << "Нижнее основание: " << bot_base << endl
    << "Высота: " << h << endl;
}

bool Trapezoid::operator==(const Trapezoid &trapezoid) {
    return bot_base == trapezoid.bot_base && top_base == trapezoid.top_base && h == trapezoid.h;
}

bool Trapezoid::operator!=(const Trapezoid &trapezoid) {
    return bot_base != trapezoid.bot_base || top_base != trapezoid.top_base || h != trapezoid.h;
}

Trapezoid &Trapezoid::operator=(const Trapezoid &trapezoid) {
    bot_base = trapezoid.bot_base;
    top_base = trapezoid.top_base;
    h = trapezoid.h;
    return *this;
}

Trapezoid::~Trapezoid() {
    bot_base = 0;
    top_base = 0;
    h = 0;
}