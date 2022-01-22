#pragma once
#include "ArrayError.h"
class ErrorIndex : public ArrayError 
{
public:
	ErrorIndex(int index);
	int List[10];
	int Index;
	bool operator == (const ErrorIndex& right) {  //overloading == operator
		return Index == right.Index;
	}
	bool operator != (ErrorIndex* const right) {  //overloading != operator
		return this != right;
	}
	ErrorIndex& operator = (const ErrorIndex& right) {  //overloading = operator
		Index = right.Index;
		return *this;
	}
};