#include <string>
#include <iostream>
#include "class.h"

int main()
{
    setlocale(0, "Russian");
    resorces* S[3];
    S[0] = new resorces("Иван", 5, 1);
    S[1] = new resorces();
    S[2] = new resorces("Виталий", 1, 1);

    S[1]->set("Дмитрий", 3, 0);

    resorces* s1 = S[1];

    for (int i = 0; i < 3; i++) S[i]->print(); //использование указателя на компоненту - функцию
    s1->print(); //использование указателя на объект
    delete[] S;
    return 0;
}