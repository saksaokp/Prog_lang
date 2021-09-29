#include "Trial.h"

list<Trial*> Trial::_list;

// Constructors
Trial::Trial(int compexity = 0, string name = "", string sponsor = "") : Test(compexity, name)
{
	this->_sponsor = sponsor;

	this->Add();
}

// Destructor
Trial::~Trial()
{
	Test::~Test();
}

// Methods
void Trial::Show()
{
	Test::Show();
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