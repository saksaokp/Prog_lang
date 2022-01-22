#ifndef YAP2_ORGANIZATION_H
#define YAP2_ORGANIZATION_H
#include<iostream>
#include<string>
#include<list>
#include<algorithm>
using namespace std;
class Organization{
protected:
    string name;
public:
    Organization(string name);
    virtual void show() = 0;
};
#endif //YAP2_ORGANIZATION_H
