#ifndef INC_3_FOURSQUARE_H
#define INC_3_FOURSQUARE_H

#include "Figure.h"

class Foursquare : public Figure {
    double a;
public:
    Foursquare();
    Foursquare(double);
    double square() override;
    double perimeter() override;
    void print() override;
    bool operator==(const Foursquare &);
    bool operator!=(const Foursquare &);
    Foursquare &operator=(const Foursquare &);
    ~Foursquare();
};


#endif //INC_3_FOURSQUARE_H
