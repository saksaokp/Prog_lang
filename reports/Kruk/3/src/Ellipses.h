#ifndef INC_3_ELLIPSES_H
#define INC_3_ELLIPSES_H

#include "Figure.h"

class Ellipses : public Figure {
    double a;
    double b;
public:
    Ellipses();
    Ellipses(double, double);
    double square() override;
    double perimeter() override;
    void print() override;
    bool operator==(const Ellipses&);
    bool operator!=(const Ellipses&);
    Ellipses& operator=(const Ellipses&);
    ~Ellipses();
};


#endif
