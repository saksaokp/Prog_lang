#ifndef UNTITLED_PRESCHOOLER_H
#define UNTITLED_PRESCHOOLER_H
#include "human.h"
#include "string"
class Preschooler :public Human {
private:
    string name;
    int age;
public:
    Preschooler();
    Preschooler(string name, int age);
    Preschooler(const Preschooler &other);
    ~Preschooler();

    bool operator == (const Preschooler &right);
    bool operator != (const Preschooler &right);
    Preschooler &operator = (const Preschooler &right);

    void Print();
    void Read();
};

#endif //UNTITLED_PRESCHOOLER_H
