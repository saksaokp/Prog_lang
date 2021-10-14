#include "Trial.h"

list<Trial*> Trial::_list;

// Constructors
Trial::Trial(int compexity = 0, string name = "", string sponsor = "") : Test(compexity, name)
{
	cout << "Trial constructor" << endl;

	this->_sponsor = sponsor;
	this->Add();
}

// Destructor
Trial::~Trial()
{
	cout << "Trial destructor" << endl;
	
	Test::~Test();
}

// Methods
void Trial::Show()
{
	cout << endl;
	cout << "Type: Trial" << endl;
	cout << "Name:" << this->_name << endl;
	cout << "Complexity: " << this->_complexity << endl;
	cout << "Sponsor: " << this->_sponsor << endl;
}

void Trial::Add()
{
	_list.push_back(this);
}

void Trial::ShowAll()
{
	for (Trial* t : Trial::_list)
	{
		t->Show();
	}
}