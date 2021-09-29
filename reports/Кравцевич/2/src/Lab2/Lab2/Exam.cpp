#include "Exam.h"

list<Exam*> Exam::_list;

// Constructors
Exam::Exam(int compexity = 0, string name = "", string subject = "") : Test(compexity, name)
{
	this->_subject = subject;

	this->Add();
}

// Destructor
Exam::~Exam()
{
	Test::~Test();
}

// Methods
void Exam::Show()
{
	Test::Show();
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