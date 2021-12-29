#include "figure.h"

void Figure::ShowVS()
{
	cout << "V = " << V() << " S = " << S() << endl;
}
bool Figure::operator==(Figure& figure)
{
	if (this->S() == figure.S() && this->V() == figure.V())
		return true;
	else
		return false;
}

bool Figure::operator!=(Figure& figure)
{
	return !(*this == figure);
}