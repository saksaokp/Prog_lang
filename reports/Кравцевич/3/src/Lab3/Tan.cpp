#include "Tan.h"

Tan::Tan()
{
	this->name = "Tan";
	this->x = 0;
	this->value = 0;
}

Tan::Tan(float x) : Tan::Tan()
{
	this->setFuncValue(x);
}

void Tan::setFuncValue(float x)
{
	this->x = x;
	this->value = tan(x);
}