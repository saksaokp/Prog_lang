#ifndef UNTITLED_SCHOOLKID_H
#define UNTITLED_SCHOOLKID_H
#include "human.h"
#include "string"
class Schoolkid :public Human {
private:
    string name;
    int age;
public:
    Schoolkid();
    Schoolkid(string name, int age);
    Schoolkid(const Schoolkid &other);
    ~Schoolkid();

    bool operator == (const Schoolkid &right);
    bool operator != (const Schoolkid &right);
    Schoolkid &operator = (const Schoolkid &right);

    void Print();
    void Read();
};
#endif //UNTITLED_SCHOOLKID_H
