#include "Auto.h"

Auto::Auto() {
    power = 1;
    price = 2;
    marka = "mers";
    get();
}

Auto::Auto(int the_power, float the_price, const char* the_marka) {
    power = the_power;
    price = the_price;
    marka = the_marka;
    get();
}
Auto::Auto(const Auto& constropy) {
    power = constropy.power;
    price = constropy.price;
    marka = constropy.marka;
}
void Auto::message() {
    cout << "about the car:" << endl;
}
void Auto::set(int the_power, float the_price, const char* the_marka) {
    power = the_power;
    price = the_price;
    marka = the_marka;
}
void Auto::get() {
    cout << " Power This auto is-" << power << ", price is-" << price << ", marka auto is-" << marka << endl;
}
Auto::~Auto() {
    cout << "auto is not working" << endl;
}