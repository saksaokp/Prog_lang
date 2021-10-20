#pragma once
#include "Function.h"

class Tan:
	virtual public Function
{
public:
	Tan();
	Tan(float x);

	void setFuncValue(float x);
};

