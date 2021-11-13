#include <windows.h>
#include "region.h"
#include "metropolis.h"

town* town::head = nullptr;
region* region::head = nullptr;
metropolis* metropolis::head = nullptr;


int main() {
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
    metropolis a1("12", 12, 12, 12, 13.2);
    metropolis a2("123", 123, 123, 1321, 187.2);
    town s1("12", 123, 123, 32);
    s1.Add();
    town* f = &a2;
    f->Show();
    return 0;
}

