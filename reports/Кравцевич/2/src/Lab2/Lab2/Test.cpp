#include "Test.h"
#include <list>

list<Test*> Test::_list;

Test::Test(int complexity = 0, string name = "")
{
	this->_complexity = complexity;
	this->_name = name;
}

Test::~Test()
{
	std::cout << "Disposed" << endl;
}

void Test::Show()
{
	cout << "Name: " << this->_name << endl;
	cout << "Complexity: " << this->_complexity << endl;
}

void Test::Add() 
{
	_list.push_back(this);
}

void Test::ShowAll()
{
	for (Test* t : Test::_list)
	{
		t->Show();
	}
}