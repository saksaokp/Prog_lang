#include "Company.h"

Company::Company(string name, int price): Organization(name) {
    this->price = price;
}

void Company::show() {
    cout<<"Name of company: "<< this->name << endl<<"Price of insurance: "<<this->price<<endl;
}

void Company::set_price(int price) {
    this->price = price;
}

int Company::get_price() {
    return this->price;
}
