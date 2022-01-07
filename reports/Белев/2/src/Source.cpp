#include "Header.h"

int person::count = 0;
person** person::persons = nullptr;

int main() {
    student michael("Michael", 19, 2);
    michael.add();
    teacher dunnig("Dunnig", 44, 12);
    teacher alex("Alex", 29, 5);
    department_head oleg("Oleg", 53, "ALOE");

    person::show();
}
