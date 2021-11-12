#pragma once
#include <iostream>
#include <vector>
#include "Function.h"


class FuncCollection 
{
public:
	std::vector<Function> functions;

	void push(Function f);
	void remove(int index);

	void display();
	int length();


	Function operator [] (int index);
};

