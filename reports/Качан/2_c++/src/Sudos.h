#ifndef YAP2_SUDOS_H
#define YAP2_SUDOS_H
#include "Organization.h"

class Sudos: public Organization{
protected:
    int number;
public:
    Sudos(string name, int number);
    void show();
    void set_number(int number);
    int get_number();
};
#endif //YAP2_SUDOS_H
