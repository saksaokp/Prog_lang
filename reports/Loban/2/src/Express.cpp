#include "Vehicle.h"
#include <iostream>

using namespace std;

Express::Express():Train()
{
	maxSpeed = 190;
    cout << "Created Express (Express())" << endl;
}
Express::Express(int speed, const char* direction, int maxSpeed, bool isAdd = false): Train(speed, direction, isAdd) {
	this->maxSpeed = maxSpeed;
	cout << "Created Express (Express(int, const char*,int, bool))" << endl;
}
Express::Express(Express& express) {
	speed = express.speed;
	maxSpeed = express.maxSpeed;
	direction = express.direction;

	cout << "Created Express (Express(Express&))" << endl;
}
Express::~Express() {
	cout << "Deleted Express" << endl;
}
void Express::Show() {
	cout << "Express. Direction:" << direction << ".Speed:" << speed <<".Max speed" << maxSpeed << endl;
}
