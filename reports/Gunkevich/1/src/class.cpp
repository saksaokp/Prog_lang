#include "class.h"
#include <iostream>
resorces::resorces() :name(0), age(0), rank(0) { std::cout << "Конструктор без параметров вызван" << std::endl; }
resorces::resorces(const char* n, int a, int g)
{
    std::cout << "Конструктор с параметрами вызван" << std::endl;
    name = n;
    age = a;
    rank = g;
}

resorces::resorces(const resorces& s)//копирующий конструктор
{
    std::cout << "Копирующий конструктор вызван" << std::endl;
    this->name = s.name;
    this->age = s.age;
    this->rank = s.rank;
}
resorces::~resorces()
{
    std::cout << "Deleting data" << std::endl;
}
void resorces::set(const char* n, int a, int g)//установка полей данных
{
    name = n;
    age = a;
    rank = g;
}
void  resorces::print()//просмотр полей данных
{
    std::cout << name << " " << age << " " << rank << std::endl;
}