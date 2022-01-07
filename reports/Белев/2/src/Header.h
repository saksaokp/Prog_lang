#include <string>
#include <iostream>
using namespace std;


class person {
public:
	const char* name;
	int age;
	static int count;
	static person** persons;
	person(const char* name, int age, bool isadd = true);
	~person();
	virtual void print() = 0;
	virtual void add();
	static void show();
};

class student : public person {
protected:
	int education_year;
public:
	student(const char* name, int age, int education_year);
	~student();
	void print();
};

class teacher : public person {
protected:
	int experience;
public:
	teacher(const char* name, int age, int experience);
	~teacher();
	void print();	
};

class department_head : public person {
protected:
	const char* department;
public:
	department_head(const char* name, int age, const char* department);
	~department_head();
	void print();
};