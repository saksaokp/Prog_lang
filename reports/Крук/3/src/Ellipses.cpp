#include "Ellipses.h"

Ellipses::Ellipses() {
    cout << "Введите малую ось: ";
    cin >> a;
    cout << "Введите большую ось: ";
    cin >> b;
    cout << endl;
}

Ellipses::Ellipses(double a, double b) {
    this->a = a;
    this->b = b;
}

double Ellipses::square() {
    return a * b * M_PI;
}

double Ellipses::perimeter() {
    return (a + b) * M_PI;
}

void Ellipses::print() {
    cout << "Элипс:" << endl
    << "Малая ось: " << a << endl
    << "Большая ось: " << b << endl;
}

bool Ellipses::operator==(const Ellipses &ellipse) {
    return (a == ellipse.a && b == ellipse.b);
}

bool Ellipses::operator!=(const Ellipses &ellipse) {
    return (a != ellipse.a || b != ellipse.b);
}

Ellipses &Ellipses::operator=(const Ellipses &ellipse) {
    a = ellipse.a;
    b = ellipse.b;
    return *this;
}

Ellipses::~Ellipses() {
    a = 0;
    b = 0;
}
