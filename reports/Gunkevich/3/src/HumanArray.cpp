#include "HumanArray.h"

HumanArray::HumanArray(int count) {
    arr = new Human*[count];
    for (int i = 0; i < count; i++) {
        arr[i] = nullptr;
    }
    this->count = count;
}
HumanArray::~HumanArray() {
    for (int i = 0; i < count; i++) {
        if (arr[i] != nullptr) {
            delete arr[i];
        }
        delete[]arr;
    }
}

Human *HumanArray::operator[] (int n) const {
    if (n < 0 || n >= count) {
        throw IndexError("You are out of bounds of an array.");
    }
    return arr[n];
}
Human *&HumanArray::operator[] (int n) {
    if (n < 0 || n >= count) {
        throw IndexError("You are out of bounds of an array.");
    }
    return arr[n];
}

int HumanArray::get_count() {
    return count;
}

void HumanArray::addToTheEnd(Human *person) {
    Human **temp = new Human*[count + 1];
    for (int i = 0; i < count; i++) {
        temp[i] = arr[i];
    }
    arr = temp;
    temp[count] = person;
    count++;
}

void HumanArray::add(int index, Human *person) {
    if (index < 0 || index > count) {
        addToTheEnd(person);
        throw IndexError("You are out of bounds of an array. The person will be added to the end of the array");
    }
    Human **temp = new Human*[count + 1];
    for (int i = 0; i < index; i++) {
        temp[i] = arr[i];
    }
    temp[index] = person;
    for (int i = index; i < count; i++) {
        temp[i + 1] = arr[i];
    }
    arr = temp;
    count++;
}

void HumanArray::deleteFromTheEnd() {
    Human **temp = new Human*[count - 1];
    for (int i = 0; i < count - 1; i++) {
        temp[i] = arr[i];
    }
    arr = temp;
    count--;
}

void HumanArray::del(int index) {
    Human **temp = new Human*[count - 1];
    for (int i = 0; i < index; i++) {
        temp[i] = arr[i];
    }
    for (int i = index + 1; i < count; i++) {
        temp[i - 1] = arr[i];
    }
    arr = temp;
    count--;
}