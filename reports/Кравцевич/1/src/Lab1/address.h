#pragma once
#include <iostream>

using namespace std;

class Address
{
public:
	void set_name(char* name);
	void set_street(char* street);
	void set_number(int number);

	char* get_name();
	char* get_street();
	int get_number();

	void display();

	Address();
	Address(char* name, char* street, int number);
	Address(Address& address);

	~Address();

private:
	char* _name;
	char* _street;
	int _number;
};
