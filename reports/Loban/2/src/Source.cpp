#include <iostream>
#include "Vehicle.h"

using namespace std;

Vehicle** Vehicle::items = nullptr;
int Vehicle::count = 0;

int main() {
	Vehicle::ShowItems();
	cout << "Create auto" << endl;
	Auto audi(50, "audi", true);
	audi.Show();
	Vehicle::ShowItems();
	cout << "Create train" << endl;
	Train train(130, "Brest", false);
	Vehicle::ShowItems();
	cout << "Add train" << endl;
	train.AddItem();
	Vehicle::ShowItems();
	cout << "Create express" << endl;
	Express trainExpress;
	cout << "Add express" << endl;
	trainExpress.AddItem();
	Vehicle::ShowItems();

}