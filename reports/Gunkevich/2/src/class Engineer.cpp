#include"class Engineer.h"
Engineer::Engineer() : Admin() {}

Engineer::Engineer(char* name, int work_experience, int salary) : Admin() {
	this->name = name;
	this->work_experience = work_experience;
	this->salary = salary;
}

void Engineer::set(char* name, int work_experience, int salary) {
	this->name = name;
	this->work_experience = work_experience;
	this->salary = salary;
}

void Engineer::show() {
	cout << "Имя: " << name << endl;
	cout << "Опыт работы(в годах): " << work_experience << endl;
	cout << "Зарплата в $: " << salary << endl;
}

Engineer::~Engineer() {}
