#pragma once
#include"class Admin.h"
class HRD :public Admin {
protected:
	char* speciality;
public:
	HRD();
	HRD(char* name, int work_experience, char* speciality);
	void set(char* name, int work_experience, char* speciality);
	void show();
	~HRD();
};