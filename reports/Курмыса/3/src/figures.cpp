#include <iostream>
#include <cmath>
#include "figures.h"

using namespace std;

Figure::Figure() {
  a = 0;
  r = 0;
  name = "Фигура";
  cout << "Создан объект класса Figure номер " << ++figures << " через конструктор по умолчанию.\n";
}

Figure::Figure(float a, float r, string name): a(a), r(r), name(name) {
  cout << "Создан объект класса Figure номер " << ++figures << " через конструктор с параметрами.\n";
}

Figure::~Figure() {
  cout << "Объект класса Figure номер " << figures-- << " успешно уничтожен.\n";
}

bool
Figure::operator ==(const Figure& right) {
  return (this->name == right.name) && (this->a == right.a) && (this->r == right.r);
}

bool
Figure::operator !=(const Figure& right) {
  return !(*this == right);
}

const Figure&
Figure::operator =(const Figure& right) {
  a = right.a;
  r = right.a;
  name = right.name;
  return *this;
}

Cube::Cube(): Figure(0, 0, "Куб") {
  cout << "Создан объект класса Cube номер " << ++cubes << " через конструктор по умолчанию.\n";
}

Cube::Cube(float a): Figure(a, 0, "Куб") {
  cout << "Создан объект класса Cube номер " << ++cubes << " через конструктор с параметрами.\n";
}

Cube::~Cube() {
  cout << "Объект класса Cube номер " << cubes-- << " успешно уничтожен.\n";
}

const float
Cube::V() const {
  return a * a * a;
}

const float
Cube::S() const {
  return 6 * a * a;
}

const void
Cube::info() const {
  cout << "Название: " << this->name << endl;
  cout << "Длина ребра a: " << this->a << endl;
  cout << "Объём V: " << this->V() << endl;
  cout << "Площадь поверхности S: " << this->S() << endl << endl;
}

Cylinder::Cylinder(): Figure(0, 0, "Цилиндр") {
  cout << "Создан объект класса Cylinder номер " << ++cylinders << " через конструктор по умолчанию.\n";
}

Cylinder::Cylinder(float a, float r): Figure(a, r, "Цилиндр") {
  cout << "Создан объект класса Cylinder номер " << ++cylinders << " через конструктор с параметрами.\n";
}

Cylinder::~Cylinder() {
  cout << "Объект класса Cylinder номер " << cylinders-- << " успешно уничтожен.\n";
}

const float
Cylinder::V() const {
  return a * r * r * (atan(1) * 4); // выражение в скобках = Pi :)
}

const float
Cylinder::S() const {
  return 2 * a * (atan(1) * 4) * r;
}

const void
Cylinder::info() const {
  cout << "Название: " << this->name << endl;
  cout << "Высота a: " << this->a << endl;
  cout << "Радиус основания r: " << this->r << endl;
  cout << "Объём V: " << this->V() << endl;
  cout << "Площадь поверхности S: " << this->S() << endl << endl;
}

Tetrahedron::Tetrahedron(): Figure(0, 0, "Тетраэдр") {
  cout << "Создан объект класса Tetrahedron номер " << ++tetrahedrons << " через конструктор по умолчанию.\n";
}

Tetrahedron::Tetrahedron(float a): Figure(a, 0, "Тетраэдр") {
  cout << "Создан объект класса Tetrahedron номер " << ++tetrahedrons << " через конструктор с параметрами.\n";
}

Tetrahedron::~Tetrahedron() {
  cout << "Объект класса Tetrahedron номер " << tetrahedrons-- << " успешно уничтожен.\n";
}

const float
Tetrahedron::V() const {
  return a * a * a / (sqrt(2) * 6);
}

const float
Tetrahedron::S() const {
  return a * a * sqrt(3);
}

const void
Tetrahedron::info() const {
  cout << "Название: " << this->name << endl;
  cout << "Длина ребра a: " << this->a << endl;
  cout << "Объём V: " << this->V() << endl;
  cout << "Площадь поверхности S: " << this->S() << endl << endl;
}