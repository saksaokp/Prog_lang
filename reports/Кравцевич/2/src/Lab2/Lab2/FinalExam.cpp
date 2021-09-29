#include "FinalExam.h"

list <FinalExam*> FinalExam::_list;

// Constructors
FinalExam::FinalExam(int compexity = 0, string name = "", string subject = "", int mark = 0) : Exam(compexity, name, subject)
{
	this->_mark = mark;

	this->Add();
}

// Destructor
FinalExam::~FinalExam()
{
	Exam::~Exam();
}

// Methods
void FinalExam::Show()
{
	Exam::Show();
	cout << "Mark: " << this->_mark << endl;
}

void FinalExam::Add()
{
	_list.push_back(this);
}

void FinalExam::ShowAll()
{
	for (FinalExam* fe : FinalExam::_list)
	{
		fe->Show();
	}
}