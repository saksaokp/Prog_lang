#include <iostream>
#include "Ticket.h"


Ticket::Ticket() :
number(0), date(0), amount(0.0)
{
    std::cout << "\n[Creating without parameters (" <<
    number << ' ' << date << ' ' << amount << ")]";
}

Ticket::Ticket(int number, int date, float amount) :
number(number), date(date), amount(amount)
{
    std::cout << "\n[Creating with parameters (" <<
        number << ' ' << date << ' ' << amount << ")]";
}

Ticket::Ticket(const Ticket& ticket) :
number(ticket.number), date(ticket.date), amount(ticket.amount)
{
    std::cout << "\n[Creating with coping (" <<
        number << ' ' << date << ' ' << amount << ")]";
}

Ticket::~Ticket() {
    std::cout << "\n[Deleting (" <<
        number << ' ' << date << ' ' << amount << ")]";
}


void Ticket::Show() const {
    std::cout << '\n' << number << ' ' << date << ' ' << amount;
}


void Ticket::SetNumber(int newNumber) {
    number = newNumber;
}

int Ticket::GetNumber() const {
    return number;
}


void Ticket::SetDate(int newDate) {
    date = newDate;
}

int Ticket::GetDate() const {
    return date;
}


void Ticket::SetAmount(float newAmount) {
    amount = newAmount;
}

float Ticket::GetAmount() const {
    return amount;
}
