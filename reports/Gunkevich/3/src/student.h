#ifndef UNTITLED_STUDENT_H
#define UNTITLED_STUDENT_H
#include "human.h"
#include "string"
class Student :public Human {
private:
    string name;
public:
    Student();
    Student(string name);
    Student(const Student &other);
    ~Student();

    bool operator == (const Student &right);
    bool operator != (const Student &right);
    Student &operator = (const Student &right);

    void Print();
    void Read();
};
#endif //UNTITLED_STUDENT_H
