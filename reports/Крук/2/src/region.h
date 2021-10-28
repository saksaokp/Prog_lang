#ifndef UNTITLED1_REGION_H
#define UNTITLED1_REGION_H
#include "place.h"
#include <iostream>

using namespace std;

class region : public place {
protected:
    static region *head ;
    region *next;
public:
    region();
    region(region &);
    region(char *, float, int);
    void Show() override;
    void Add() override;
    static void Show_list();
    ~region();
};

#endif //UNTITLED1_REGION_H
