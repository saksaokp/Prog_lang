#pragma once
#include "Function.h"

class Sin : 
	virtual public Function
{
public:
	Sin();
	Sin(float x);

	void setFuncValue(float x);
};

