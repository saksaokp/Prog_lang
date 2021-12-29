#include"class Worker.h"

Worker::Worker() : HRD() {}

Worker::Worker(char* name, int work_experience, char* speciality, int pass) : HRD(name, work_experience, speciality) {
	this->name = name;
	this->work_experience = work_experience;
	this->speciality = speciality;
	this->pass = pass;
}

void Worker::set(char* name, int work_experience, char* speciality, int pass) {
	this->name = name;
	this->work_experience = work_experience;
	this->speciality = speciality;
	this->pass = pass;
}

void Worker::show() {
	cout << "Имя: " << name << endl;
	cout << "Опыт работы(в годах): " << work_experience << endl;
	cout << "Специальность: " << speciality << endl;
	cout << "Количество пропусков без причины: " << pass << endl;
}

Worker::~Worker() {}
