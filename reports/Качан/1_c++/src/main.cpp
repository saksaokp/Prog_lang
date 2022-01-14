#include <iostream>
#include "Library.h"
using namespace std;

int main() {
    Library l1;
    Library l2("2_book", "M. Lermontov", 54.33);
    Library l3(l1);
    Library* l4 = new Library("3_book", "M. Tank", 35.55);

    l1.Show();
    l4->SetPrice(75.25);
    l4->Show();
    l3.Show();

    void(Library:: * pointer_show)();
    pointer_show = &Library::Show;
    (l2.*pointer_show)();

}

