//
// Created by DualistOFFsetWOT on 30.10.2021.
//
#include "Auto.h"


int main(int argc, const char* argv[]) {
    Auto shkoda(100, 200, "Shkoda");
    shkoda.message();
    shkoda.set(3000, 100000, "Shkoda");
    shkoda.get();


    Auto BMW;
    BMW.message();
    BMW.set(5000, 1000000, "BMW");
    BMW.get();


    Auto* TESLA = new Auto;
    TESLA->message();
    TESLA->set(9999, 99999, "TESLA");
    void(Auto:: * pisec)();
    pisec = &Auto::get;
    (TESLA->*pisec)();
    cin.get();
    delete TESLA;
    return 0;


}

