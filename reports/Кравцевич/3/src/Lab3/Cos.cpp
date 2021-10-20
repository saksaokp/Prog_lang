#include "Cos.h"

Cos::Cos()
{
	this->name = "Cos";
	this->x = 0;
	this->value = 0;
}

Cos::Cos(float x) : Cos::Cos()
{
	this->setFuncValue(x);
}

void Cos::setFuncValue(float x)
{
	this->x = x;
	this->value = cos(x);
}
