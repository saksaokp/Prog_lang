#include "Vehicle.h"
#include <iostream>

using namespace std;
Auto::Auto()
{
	speed = 40;
	marka = "Audi";
	cout << "Created Vehicle (Auto())" << endl;
}
Auto::Auto(int speed, const char* marka, bool isAdd = false):Vehicle(speed, isAdd) {
	this->marka = marka;
	cout << "Created Auto (Auto(int, const char*, bool))" << endl;
}
Auto::Auto(Auto& _auto) {
	speed = _auto.speed;
	marka = _auto.marka;
	cout << "Created Auto (Auto(&))" << endl;
}
Auto::~Auto() {
	cout << "Deleted Auto" << endl;
}

void Auto::Show() {
	cout << "Auto. Marka:" << marka << ".Speed:" << speed << endl;
}