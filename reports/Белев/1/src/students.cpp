#include "Header.h"

student::student() { 
	cout << "\nCreated empty object"; 
};
student::student(string n, int y, bool s) {
	name = n; 
	year = y; 
	sex = s; 
};
student::student(student& testobj) : 
	name(testobj.name), 
	year(testobj.year), 
	sex(testobj.sex) 
{};
student::~student() { 
	cout << "\nObject deleted"; 
};
void student::set(string n, int y, bool s) { 
	name = n; 
	year = y; 
	sex = s; 
};
void student::print() { 
	cout << "\n" << name << " " << " " << year << " " << sex; 
}
float student::divideyear(float divider) {
	return year / divider;
};