#include <iostream>
#include "classes.h"
using namespace std;


SaleItem::SaleItem(const char *name, float price, bool isAdd) :
name(name), price(price) {
    if (isAdd) add();
    cout << "Created SaleItem \"" << name << "\"\n";
}

SaleItem::~SaleItem() {
    cout << "Deleted SaleItem \"" << name << "\"\n";
}

void SaleItem::add() {
    SaleItem** temp = items;
    items = new SaleItem* [count + 1];
    for(int i = 0; i < count; i++)
        items[i] = temp[i];
    items[count] = this;
    count++;
}

void SaleItem::showItems() {
    for(int i=0; i<count; i++)
        items[i]->print();
}


Toy::Toy(const char *name, float price, int min_age) :
SaleItem(name, price, false), min_age(min_age) {
    cout << "Created Toy \"" << name << "\"\n";
}

Toy::~Toy() {
    cout << "Deleted Toy \"" << name << "\"\n";
}

void Toy::print() {
    cout << "Toy with name: \"" << name << "\", price: " << price << ", min_age: " << min_age << "\n";
}


Product::Product(const char *name, float price, int isAlcoholic) :
SaleItem(name, price, true), isAlcoholic(isAlcoholic) {
    cout << "Created Product \"" << name << "\"\n";
}

Product::~Product() {
    cout << "Deleted Product \"" << name << "\"\n";
}

void Product::print() {
    cout << "Product with name: \"" << name << "\", price: " << price << ", isAlcoholic: " << isAlcoholic << "\n";
}


MilkProduct::MilkProduct(const char *name, float price, int isAlcoholic, float fatness) :
Product(name, price, isAlcoholic), fatness(fatness) {
    cout << "Created MilkProduct \"" << name << "\"\n";
}

MilkProduct::~MilkProduct() {
    cout << "Deleted MilkProduct \"" << name << "\"\n";
}

void MilkProduct::print() {
    cout << "MilkProduct with name: \"" << name << "\", price: " << price
         << ", isAlcoholic: " << isAlcoholic << ", fatness " << fatness << "\n";
}
