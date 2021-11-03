#ifndef UNTITLED_WORKER_H
#define UNTITLED_WORKER_H
#include "human.h"
#include "string"
class Worker :public Human {
private:
    string name;
public:
    Worker();
    Worker(string name);
    Worker(const Worker &other);
    ~Worker();

    bool operator == (const Worker &right);
    bool operator != (const Worker &right);
    Worker &operator = (const Worker &right);

    void Print();
    void Read();
};
#endif //UNTITLED_WORKER_H
