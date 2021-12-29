#ifndef UNTITLED1_PLACE_H
#define UNTITLED1_PLACE_H

#include <iostream>

using namespace std;

class place {
public:
    place();
    place(place &);
    place(char *, float, int);
    virtual void Add() = 0;
    virtual void Show() = 0;
    void setName(char *name);
    void setSquare(float square);
    void setPopulations(int populations);
    ~place();

protected:
    char *name{};
    float square;
    int populations;
};

#endif
