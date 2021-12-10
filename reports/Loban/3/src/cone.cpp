#include "figure.h"


Cone::Cone(double r, double h, double l, double so) : r(r), Pyramid(h, l, pi* r * 2, so) {}

double Cone::S() {
	return so + pi * r * l;
}
void Cone::Show() {
	cout << "Cone. R = " << r << " H = " << h << " So = " << so << endl;
}
Cone& Cone::operator=(Cone& cone) {
	this->r = cone.r;
	this->h = cone.h;
	this->l = cone.l;
	this->so = cone.so;

	return *this;
}