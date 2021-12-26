#include "engine.h"
void Engine::add() {
    objects.push_back(this);
}

void Engine::print() {
    int num = 0;
    for (Engine* obj : objects) {
        num++;
        cout << num << "-";
        obj->show();
    }
}

void Combustion_engine::show() {
    cout << "Power: " << power_r << "\nCost: " << cost_t << "\nFuel: " << fuel_l << endl;
}

void Diesel::show() {
    cout << "Power: " << power_r << "\nCost: " << cost_t << "\nFuel: " << fuel_l << "\nTransport: " << transport_t << endl;
}

void Turbojet_engine::show() {
    cout << "Power: " << power_r << "\nCost: " << cost_t << "\nVendor: " << vendor_r << endl;
}


Engine::Engine(int power, float cost)
    : power_r(power), cost_t(cost) {
    cout << "Constructor for engine" << endl;
    add();
}

Combustion_engine::Combustion_engine(int power, float cost, int fuel)
    : Engine(power, cost), fuel_l(fuel) {
    cout << "Constructor for Combustion engine" << endl;
}

Diesel::Diesel(int power, float cost, int fuelL, string transport)
    : Combustion_engine(power, cost, fuelL), transport_t(transport) {
    cout << "Constructor for Diesel" << endl;
}

Engine::~Engine() {
    cout << "Destructor for engine" << endl;
}

Combustion_engine::~Combustion_engine() {
    cout << "Destructor for Combustion " << endl;
}

Diesel::~Diesel() {
    cout << "Destructor for Diesel" << endl;
}

Turbojet_engine::~Turbojet_engine() {
    cout << "Destructor for Turbojet" << endl;
}

Turbojet_engine::Turbojet_engine(int power, float cost, string vendor)
    : Engine(power, cost), vendor_r(vendor) {
    cout << "Constructor for turbojet engine" << endl;
}
