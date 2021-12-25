#pragma once
#include"class Admin.h"
class Engineer :public Admin {
protected:
	int salary;
public:
	Engineer();
	Engineer(char* name, int work_experience, int salary); 
	void set(char* name, int work_experience, int salary);
	void show();
	~Engineer();
};
