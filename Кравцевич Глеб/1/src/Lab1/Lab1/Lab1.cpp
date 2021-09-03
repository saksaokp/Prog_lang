#include <iostream>
#include "address.h"

using namespace std;

int main()
{
    Address* address_empty = new Address();
    address_empty->display();

    address_empty->set_name("Name");

    Address* address_valid = new Address("Name", "Street", 15);
    address_valid->display();

    Address* address_copy = new Address(*address_valid);
    address_copy->display();

    delete address_empty;
    delete address_valid;
    delete address_copy;

    getchar();
    return 0;
}
