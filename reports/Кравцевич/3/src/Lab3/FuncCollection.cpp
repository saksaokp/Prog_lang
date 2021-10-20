#include "FuncCollection.h"

void FuncCollection::push(Function f)
{
	this->functions.push_back(f);
}

int FuncCollection::length()
{
	return this->functions.size();
}

void FuncCollection::remove(int index)
{
	if (index >= this->functions.size())
	{
		throw out_of_range("Index out of range exception");
	}

	this->functions.erase(this->functions.begin() + index);
}

Function FuncCollection::operator [] (int index)
{
	if (index >= this->functions.size())
	{
		throw out_of_range("Index out of range exception");
	}

	return this->functions[index];
}

void FuncCollection::display()
{
	for (size_t i = 0; i < this->length(); i++)
	{
		std::cout << i << ": " << this->functions[i].toString() << std::endl;
	}
}