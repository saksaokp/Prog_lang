#ifndef INC_3_TRAPEZOID_H
#define INC_3_TRAPEZOID_H

#include "Figure.h"

class Trapezoid : public Figure{
    double bot_base;
    double top_base;
    double h;
public:
    Trapezoid();
    Trapezoid(double, double, double);
    double square() override;
    double perimeter() override;
    void print() override;
    bool operator==(const Trapezoid &);
    bool operator!=(const Trapezoid &);
    Trapezoid &operator=(const Trapezoid &);
    ~Trapezoid();
};


#endif
