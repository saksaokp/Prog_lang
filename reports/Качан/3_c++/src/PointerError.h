#pragma once
#include "ArrayError.h"
class PointerError : public ArrayError 
{
public:
	PointerError(int *ptr);
	int* Pointer;
	bool operator == (const PointerError& right) {  //overloading == operator
		return Pointer == right.Pointer;
	}
	bool operator != (PointerError* const right) {  //overloading != operator
		return this != right;
	}
	PointerError& operator = (const PointerError& right) {  //overloading = operator
		Pointer = right.Pointer;
		return *this;
	}
};
