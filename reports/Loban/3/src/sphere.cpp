#include "figure.h"

Sphere::Sphere(double r) : r(r) {}

double Sphere::V(){
	return (4 * r * r * r * pi) / 3;
}

double Sphere::S(){
	return 4 * pi * r * r;
}
void Sphere::Show(){
	cout << "Sphere. R = " << r << endl;
}

Sphere& Sphere::operator=(Sphere& sphere) {
	this->r = sphere.r;
	return *this;
}