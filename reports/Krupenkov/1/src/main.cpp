#include <iostream>
#include "Ticket.h"


int main() {
    auto* t1 = new Ticket;
    // Использование конструктора без параметра
    auto* t2 = new Ticket(1, 2, 3);
    // Использование конструктора с параметрами
    auto* t3 = new Ticket(*t2);
    // Использование конструктора копирования
    auto* t4 = new Ticket(Ticket(3, 3, 7));
    // Элизия (умное слово) - копирование анонимного объекта
    // В таких случаях компилятору разрешается отказаться от вызова
    // конструктора копирования и просто выполнить стандартный конструктор.


    t1->SetNumber(3);
    std::cout << '\n' << t1->GetNumber();
    t1->Show();

    t2->SetDate(9);
    std::cout << '\n' << t2->GetDate();
    t2->Show();

    t3->SetAmount(t4->GetAmount());
    std::cout << '\n' << t3->GetAmount();

    // Указатель на метод
    void (Ticket::*showPtr)() const;
    showPtr = &Ticket::Show;
    (t3->*showPtr)();

    delete t1;
    delete t2;
    delete t3;
    delete t4;
}
