#include"class HRD.h"
HRD::HRD() : Admin() {}

HRD::HRD(char* name, int work_experience, char* speciality) : Admin() {
	this->name = name;
	this->work_experience = work_experience;
	this->speciality = speciality;
}

void HRD::set(char* name, int work_experience, char* speciality) {
	this->name = name;
	this->work_experience = work_experience;
	this->speciality = speciality;
}

void HRD::show() {
	cout << "Имя: " << name << endl;
	cout << "Опыт работы(в годах): " << work_experience << endl;
	cout << "Специальность: " << speciality << endl;
}

HRD::~HRD() {}