#include "worker.h"
Worker::Worker() {}
Worker::Worker(string name) {
    this->name = name;
}
Worker::Worker(const Worker &other) {
    name = other.name;
}
Worker::~Worker() {}

bool Worker::operator == (const Worker &right) {
    return name == right.name;
}
bool Worker::operator != (const Worker &right) {
    return !(*this == right);
}
Worker &Worker::operator = (const Worker &right) {
    name = right.name;
    return *this;
}

void Worker::Print() {
    cout << endl << "Name of worker: " << name << endl;
}
void Worker::Read() {
    cout << endl << "Enter the name of worker: ";
    cin >> name;
}