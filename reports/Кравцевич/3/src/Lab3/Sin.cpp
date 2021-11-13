#include "Sin.h"

Sin::Sin()
{
	this->name = "Sin";
	this->x = 0;
	this->value = 0;
}

Sin::Sin(float x) : Sin::Sin()
{
	this->setFuncValue(x);
}

void Sin::setFuncValue(float x)
{
	this->x = x;
	this->value = sin(x);
}