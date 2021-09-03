#ifndef TICKET_H
#define TICKET_H


class Ticket {
    int number;
    int date;
    float amount;

public:
    Ticket();
    Ticket(int number, int date, float amount);
    Ticket(const Ticket& ticket);
    ~Ticket();

    void Show() const;

    void SetNumber(int newNumber);
    int GetNumber() const;
    void SetDate(int newDate);
    int GetDate() const;
    void SetAmount(float newAmount);
    float GetAmount() const;

};

#endif //TICKET_H
