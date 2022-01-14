#ifndef YAP2_COMPANY_H
#define YAP2_COMPANY_H
#include "Organization.h"

class Company: public Organization{
protected:
    int price;
public:
    Company(string name, int price);
    void show();
    void set_price(int price);
    int get_price();
};
#endif //YAP2_COMPANY_H
