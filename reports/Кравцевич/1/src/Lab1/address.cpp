#include <iostream>
#include "address.h"

using namespace std;

void Address::set_name(char* name)
{
	Address::_name = name;
}

void Address::set_street(char* street)
{
	Address::_street = street;
}

void Address::set_number(int number)
{
	Address::_number = number;
}

char* Address::get_name()
{
	return Address::_name;
}

char* Address::get_street()
{
	return Address::_street;
}

int Address::get_number()
{
	return Address::_number;
}

void Address::display()
{
	if (Address::_name == NULL || Address::_street == NULL)
	{
		cout << "Empty values" << endl;
		return;
	}

	cout << "Address: " << _name << " " << _street << " " << _number << endl;
}

Address::Address()
{
	cout << "Created new address" << endl;
	Address::_name = NULL;
	Address::_street = NULL;
	Address::_number = -1;
}

Address::Address(char* name, char* street, int number)
{
	Address::_name = name;
	Address::_street = street;
	Address::_number = number;
}

Address::Address(Address& address)
{
	Address::_name = address.get_name();
	Address::_street = address.get_street();
	Address::_number = address.get_number();
}

Address::~Address()
{
	cout << "Address disposed" << endl;
}