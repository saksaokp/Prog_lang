#include"class Admin.h"
#include"class Worker.h"
#include"class HRD.h"
#include"class Engineer.h"
#include <iostream>

int main() {
	setlocale(LC_ALL, "rus");
	char* name = new char[100];
	cout << "Enter the name:" << endl;
	cin.getline(name, 100);
	Engineer object1(name, 5, 900);
	Engineer p = object1;

	object1.show();
	cout << endl;
	name = new char[100];
	char* speciality = new char[100];
	cout << "Enter the name:" << endl;
	cin.getline(name, 100);
	cout << "Enter speciality:" << endl;
	cin.getline(speciality, 100);
	HRD* object2 = new HRD(); //добавление объекта в список при его создании
	object2->set(name, 3, speciality);
	object2->show();
	cout << endl;
	name = new char[100];
	speciality = new char[100];
	cout << "Enter the name:" << endl;
	cin.getline(name, 100);
	cout << "Enter speciality:" << endl;
	cin.getline(speciality, 100);
	Worker object3 = Worker();
	object3.set(name, 2, speciality, 3);
	object3.show();
	cout << endl;
	Admin::look_up_list();
	delete object2;
	delete[] name;
	delete[] speciality;
	return 0;
}
