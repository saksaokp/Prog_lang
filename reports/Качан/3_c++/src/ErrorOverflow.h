#pragma once
#define list_max_index 10
#include "ArrayError.h"
class ErrorOverflow :public ArrayError
{
public:
	ErrorOverflow(int index);
	int List[10];
	int Index;
	bool operator == (const ErrorOverflow& right) {  //overloading == operator
		return Index == right.Index;
	}
	bool operator != (ErrorOverflow* const right) {  //overloading != operator
		return this != right;
	}
	ErrorOverflow& operator = (const ErrorOverflow& right) {  //overloading = operator
		Index = right.Index;
		return *this;
	}
};
