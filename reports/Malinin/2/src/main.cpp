#include "engine.h"

list <Engine*> Engine::objects{};

int main() {
    Combustion_engine first(1, 2, 3);
    Diesel second(1, 2, 3, "stop");
    Combustion_engine third(1, 2, 3);
    Turbojet_engine forth(1, 2, "Tesla");
    Engine::print();
}