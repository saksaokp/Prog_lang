#include "Header.h"

person::person(const char* name, int age, bool isadd) :
	name(name), age(age) {
	if (isadd) add();
	cout << "Person " << name << " created\n";
}
person :: ~person() {
	cout << "Person " << name << " deleted\n";
}
void person::add() {
	person** temp = persons;
	persons = new person * [count + 1];
	for (int i = 0; i < count; i++)
		persons[i] = temp[i];
	persons[count] = this;
	count++;
}
void person::show() {
	for (int i = 0; i < count; i++)
		persons[i]->print();
}


student::student(const char* name, int age, int education_year) :
	person(name, age, false), education_year(education_year) {
	cout << "Student " << name << " created\n";
}
student :: ~student() {
	cout << "Student " << name << " deleted\n";
}
void student::print() {
	cout << "Student name: " << name << " Age: " << age << " Education year: " << education_year << "\n";
}

teacher::teacher(const char* name, int age, int experience) :
	person(name, age, true), experience(experience) {
	cout << "Teacher " << name << " created\n";
}
teacher :: ~teacher() {
	cout << "Student " << name << " deleted\n";
}
void teacher::print() {
	cout << "Teacher name: " << name << " Age: " << age << " Experience: " << experience << "\n";
}

department_head::department_head(const char* name, int age, const char * department) :
	person(name, age, true), department(department) {
	cout << "Head of the Department " << name << " created\n";
}
department_head :: ~department_head() {
	cout << "Head of the Department " << name << " deleted\n";
}
void department_head::print() {
	cout << "Head of the Department name: " << name << " Age: " << age << " Department: " << department << "\n";
}
