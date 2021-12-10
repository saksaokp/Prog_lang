#include "Vehicle.h"
#include <iostream>
using namespace std;

Vehicle::Vehicle()
{
	speed = 40;
	cout << "Created Vehicle (Vehicle())" << endl;
}
Vehicle::Vehicle(int speed, bool isAdd = false) {
	this->speed = speed;
	if (isAdd) {
		AddItem();
	}
	cout << "Created Vehicle (Vehicle(int, bool))" << endl;
}
Vehicle::Vehicle(Vehicle& vehicle) {
	speed = vehicle.speed;
	cout << "Created Vehicle (Vehicle(Vehicle&))" << endl;
}
Vehicle::~Vehicle() {
	cout << "Deleted Vehicle" << endl;
}
void Vehicle::AddItem()
{
	++Vehicle::count;
	Vehicle** tempItems = items;
	items = new Vehicle * [count];
	for (int i = 0; i < count - 1;i++) {
		items[i] = tempItems[i];
	}
	items[count - 1] = this;
	delete tempItems;
}

void Vehicle::ShowItems() {
	cout << "Items:" << endl;
	for (int i = 0; i < count; i++) {
		items[i]->Show();
	}
}