#include "Test.h"
#include <list>

list<Test*> Test::_list;

Test::Test(int complexity = 0, string name = "")
{
	std::cout << "Test constructor" << endl;

	this->_complexity = complexity;
	this->_name = name;
}

Test::~Test()
{
	std::cout << "Test destructor" << endl;
}
