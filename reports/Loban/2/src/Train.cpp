#include "Vehicle.h"
#include <iostream>

using namespace std;

Train::Train():Vehicle()
{
	direction = "Minsk";
	cout << "Created Train (Train())" << endl;
}
Train::Train(int speed, const char* direction, bool isAdd = false):Vehicle(speed, isAdd) {
	this->direction = direction;
	cout << "Created Train (Train(int, const char*, bool))" << endl;
}
Train::Train(Train& train) {
	speed = train.speed;
	direction = train.direction;
	cout << "Created Train (Train(Train&))" << endl;
}
Train::~Train() {
	cout << "Deleted Train" << endl;
}
void Train::Show() {
	cout << "Train. Direction:" << direction << ".Speed:" << speed << endl;
}