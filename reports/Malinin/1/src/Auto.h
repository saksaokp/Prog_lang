#ifndef UNTITLED_AUTO_H
#define UNTITLED_AUTO_H

#endif //UNTITLED_AUTO_H
#pragma once
#include <iostream>
using namespace std;

class Auto {
private:
    int power;
    float price;
    const char* marka;

public:
    Auto();
    Auto(int the_power, float the_price, const char* the_marka);
    Auto(const Auto& constropy);
    void message();
    void set(int the_power, float the_price, const char* the_marka);
    void get();
    ~Auto();
};