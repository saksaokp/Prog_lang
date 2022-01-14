#ifndef YAP2_FACTORY_H
#define YAP2_FACTORY_H
#include "Sudos.h"
#include "Organization.h"
class Factory: public Sudos{
protected:
    string position;
public:
    Factory(string name, int number, string position);
    void show();
    void set_position(string position);
    string get_position();
};
#endif //YAP2_FACTORY_H
