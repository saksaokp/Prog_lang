#pragma once
#include <math.h>
#include <string>

using namespace std;

class Function
{
public:
	float value;
	float x;
	string name = "Simple function";

	Function();
	Function(float x);
	~Function() { }

	virtual void setFuncValue(float x);

	string toString();

	void operator = (float v);
	bool operator == (Function rightFunction);
	bool operator != (Function rightFunction);

	Function operator / (Function rightFunction);
};

