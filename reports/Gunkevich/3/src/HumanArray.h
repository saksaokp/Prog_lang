#ifndef UNTITLED_HUMANARRAY_H
#define UNTITLED_HUMANARRAY_H
#include "human.h"
#include "error.h"
class HumanArray {
private:
    Human **arr;
    int count;
public:
    HumanArray(int count);
    ~HumanArray();
    Human* operator[] (int n) const;
    Human*& operator[] (int n);
    int get_count();
    void addToTheEnd(Human *person);
    void add(int index, Human *person);
    void deleteFromTheEnd();
    void del(int index);
};

#endif //UNTITLED_HUMANARRAY_H
