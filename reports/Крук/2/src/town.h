#ifndef UNTITLED1_TOWN_H
#define UNTITLED1_TOWN_H
#include "place.h"

class town : public place{
protected:
    int year;
    static town *head;
    town *next;
public:
    town();
    town(town &);
    town(char *, float, int, int);
    void Show() override;
    void Add() override;
    void setYear(int year);
    static void Show_list();
    ~town();
};

#endif //UNTITLED1_TOWN_H
