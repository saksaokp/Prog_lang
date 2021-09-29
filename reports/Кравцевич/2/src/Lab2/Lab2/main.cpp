#include <iostream>
#include "Exam.h"
#include "FinalExam.h"
#include "Trial.h"

int main()
{
	Exam e(1, "name", "subject");
	Exam e2(2, "name2", "subject2");
	
	FinalExam fe(1, "fname", "fsubject", 10);
	FinalExam fe2(2, "fname2", "fsubject2", 12);

	Trial t(1, "tname", "sponsor");
	Trial t2(2, "tname2", "sponsor2");

	Exam::ShowAll();
	cout << "\n";
	FinalExam::ShowAll();
	cout << "\n";
	Trial::ShowAll();

	getchar();
}
