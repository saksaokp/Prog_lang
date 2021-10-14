#pragma once
#include <list>
#include <iostream>
#include <string>

using namespace std;

class Test
{
private:
	static list<Test*> _list;

protected:
	string _name;
	int _complexity;

public:
	Test(int, string);

	virtual ~Test();
	virtual void Add() = 0;
	virtual void Show() = 0;

	static void ShowAll();	
};

