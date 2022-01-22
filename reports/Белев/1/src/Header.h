#ifndef STUDENTH
#define STUDENTH
#include <iostream>
using namespace std;

class student {
private:
	string name;
	int year;
	bool sex;
public:
	student() ;
	student(string n, int y, bool s);
	student(student& testobj);
	~student();
	void set(string n, int y, bool s);
	void print();
	float divideyear(float divider);
};

#endif