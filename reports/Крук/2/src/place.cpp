#include "place.h"

place::place() {
    name = new char[100];
    square = 0;
    populations = 0;
}

place::place(place &copy) {
    name = copy.name;
    square = copy.square;
    populations = copy.populations;
}

place::place(char *new_name, float new_square, int new_populations) {
    name = new_name;
    square = new_square;
    populations = new_populations;
}

void place::setName(char *name) {
    place::name = name;
}

void place::setSquare(float square) {
    place::square = square;
}

void place::setPopulations(int populations) {
    place::populations = populations;
}

place::~place() {
    delete name;
};
