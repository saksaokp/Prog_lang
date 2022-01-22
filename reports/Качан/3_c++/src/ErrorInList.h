#pragma once
#include "ArrayError.h"
class ErrorInList :public ArrayError 
{
public:
	ErrorInList(int value);
	int List[10];
};
