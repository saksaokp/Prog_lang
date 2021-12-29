#include "figure.h"

Pyramid::Pyramid(double h, double l, double po, double so) : h(h), l(l), po(po), so(so) {}

double Pyramid::V() {
	return (so * h) / 3;
}
double Pyramid::S() {
	return (l * po) / 2 + so;
}
void Pyramid::Show() {
	cout << "Pyramid. H = " << h << " L = " << l << " Po = " << po << " So = " << so << endl;
}

Pyramid& Pyramid::operator=(Pyramid& pyramid)
{
	this->h = pyramid.h;
	this->l = pyramid.l;
	this->so = pyramid.so;
	this->po = pyramid.po;

	return *this;
}