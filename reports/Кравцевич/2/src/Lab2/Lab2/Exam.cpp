#include "Exam.h"

list<Exam*> Exam::_list;

// Constructors
Exam::Exam(int compexity = 0, string name = "", string subject = "") : Test(compexity, name)
{
	cout << "Exam constructor" << endl;

	this->_subject = subject;
	this->Add();
}

// Destructor
Exam::~Exam()
{
	cout << "Exam destructor" << endl;

	Test::~Test();
}

// Methods
void Exam::Show()
{
	cout << endl;
	cout << "Type: Exam" << endl;
	cout << "Name:" << this->_name << endl;
	cout << "Complexity: " << this->_complexity << endl;
	cout << "Subject: " << this->_subject << endl;
}

void Exam::Add()
{
	_list.push_back(this);
}

void Exam::ShowAll()
{
	for (Exam* e : Exam::_list)
	{
		e->Show();
	}
}