#include <iostream>
#include "Ticket.h"


int main() {
    Ticket t1;
    // Использование конструктора без параметра
    Ticket t2(1, 2, 3);
    // Использование конструктора с параметрами
    Ticket t3(t2);
    // Использование конструктора копирования
    Ticket t4(Ticket(3, 3, 7));
    // Элизия (умное слово) - копирование анонимного объекта
    // В таких случаях компилятору разрешается отказаться от вызова
    // конструктора копирования и просто выполнить стандартный конструктор.

    t1.Show();
    t2.Show();
    t3.Show();
    t4.Show();

    t1.SetNumber(3);
    std::cout << '\n' << t1.GetNumber();
    t2.SetDate(9);
    std::cout << '\n' << t2.GetDate();
    t3.SetAmount(t4.GetAmount());
    std::cout << '\n' << t3.GetAmount();

    t1.Show();
    t2.Show();
    t3.Show();
    t4.Show();
}
