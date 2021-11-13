#ifndef INC_3_FIGURE_H
#define INC_3_FIGURE_H

#include <iostream>
#include "math.h"

using namespace std;


class Figure {
public:
    virtual double square() = 0;
    virtual double perimeter() = 0;
    virtual void print() = 0;
};


#endif
