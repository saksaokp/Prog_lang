#pragma once
#include"class HRD.h"
class Worker :public HRD {
protected:
	int pass;
public:
	Worker();
	Worker(char* name, int work_experience, char* speciality, int pass);
	void set(char* name, int work_experience, char* speciality, int pass);
	void show();
	~Worker();
};
