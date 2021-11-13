#include <iostream>
#include "address.h"

using namespace std;

int main()
{
	Address* address_empty = new Address();
	address_empty->display();

	char name[] = "Name";
	char street[] = "Street";
	address_empty->set_name(name);

	Address* address_valid = new Address(name, street, 15);
	address_valid->display();

	Address* address_copy = new Address(*address_valid);
	address_copy->display();

	void (Address:: * pointer)();
	pointer = &Address::display;

	Address address(name, street, 10);
	(address.*pointer)();
	
	delete address_empty;
	delete address_valid;
	delete address_copy;

	getchar();
	return 0;
}
