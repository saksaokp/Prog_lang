#include <iostream>
#include <cmath>
#include "number.h"

using namespace std;

Number::Number() {
	a = 0;
	f = 0;
	i = 0;
	name = "Chislo";
	cout << "Cree obj class Number nomer " << ++numbers << " 4erez constr po ymolch.\n";
}

Number::Number(int a, int f, float i, string name) : a(a), f(f), i(i), name(name) {
	cout << "Cree obj class Number nomer " << ++numbers << " 4erez constr s parametrami.\n";
}

Number::~Number() {
	cout << "Obj class Number nomer " << numbers-- << " delete.\n";
}

bool
Number::operator ==(const Number& right) {
	return (this->a == right.a) && (this->f == right.f) && (this->i == right.i) && (this->name == right.name);
}

bool
Number::operator !=(const Number& right) {
	return !(*this == right);
}

const Number&
Number::operator =(const Number& right) {
	a = right.a;
	f = right.f;
	i = right.i;
	name = right.name;
	return *this;
}

Integer::Integer() : Number(0, 0, 0, "Celoe") {
	cout << "Creet jbj class Integer nomer " << ++integers << " 4erez constr po ymolch.\n";
}

Integer::Integer(int a) : Number(a, 0, 0, "Целое") {
	cout << "Creet obj class Integer nomer " << ++integers << " 4erez constr s parametrami.\n";
}

Integer::~Integer() {
	cout << "Creet obj class Integer nomer " << integers-- << " delete.\n";
}

const void
Integer::out() const {
	cout << this->a;
}

const void
Integer::info() const {
	cout << "Nazvanie: " << this->name << endl;
	cout << "Celaya chast: " << this->a << endl;
	cout << "Zapis number: "; this->out(); cout << endl << endl;
}

Real::Real() : Number(0, 0, 0, "Veshestvennoe") {
	cout << "Creet Obj class REAL nomer " << ++reals << " 4erez constr po ymolch.\n";
}

Real::Real(int a, int f) : Number(a, f, 0, "Veshestvennoe") {
	cout << "Creet Obj class REAL nomer " << ++reals << " 4erez constr s parametrami..\n";
}

Real::~Real() {
	cout << "OBJ class REAL nomer " << reals-- << " delete.\n";
}

const void
Real::out() const {
	cout << this->a << '.' << this->f;
}

const void
Real::info() const {
	cout << "Nazvanie: " << this->name << endl;
	cout << "Celaya chast: " << this->a << endl;
	cout << "Veshestvennaya chast: " << this->f << endl;
	cout << "Zapis chisla: "; this->out(); cout << endl << endl;
}

Complex::Complex() : Number(0, 0, 0, "Comlex") {
	cout << "Creet Obj class Complex nomer " << ++complexes << " 4erez constr po ymolch.\n";
}

Complex::Complex(int a, int f, float i) : Number(a, f, i, "Complex") {
	cout << "Creet Obj class Complex nomer " << ++complexes << " 4erez constr s parametrami.\n";
}

Complex::~Complex() {
	cout << "Obj class Complex nomer " << complexes-- << " delete.\n";
}

const void
Complex::out() const {
	cout << this->a << '.' << this->f << '+' << this->i << 'i';
}

const void
Complex::info() const {
	cout << "Nazvamie: " << this->name << endl;
	cout << "Celaya chast: " << this->a << endl;
	cout << "vesh chast: " << this->f << endl;
	cout << "complex chast: " << this->i << endl;
	cout << "zapis chisla: "; this->out(); cout << endl << endl;
}