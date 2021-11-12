#include "Function.h"

Function::Function()
{
	this->x = 0;
	this->value = 0;
}

Function::Function(float x)
{
	this->setFuncValue(x);
}

void Function::setFuncValue(float x)
{
	this->x = x;
	this->value = x;
}

string Function::toString()
{
	return this->name + "(" + to_string(this->x) + ") = " + to_string(this->value);
}

bool Function::operator == (Function rightFunction)
{
	return this->value == rightFunction.value;
}

bool Function::operator != (Function rightFunction)
{
	return this->value != rightFunction.value;
}

void Function::operator = (float v)
{
	this->setFuncValue(v);
}

Function Function::operator / (Function rightFunction)
{
	Function result;
	result.value = this->value / rightFunction.value;
	
	return result;
}
