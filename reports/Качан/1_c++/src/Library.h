#ifndef YAP1_LIBRARY_H
#define YAP1_LIBRARY_H

#include<iostream>
using namespace std;

class Library {
    string name;
    string author;
    float price;
public:
    Library();
    Library(string Name, string Author, float Price);
    Library(const Library&lib);
    ~Library();
    string GetName();
    string GetAuthor();
    float GetPrice();
    void SetName(string);
    void SetAuthor(string);
    void SetPrice(float);
    void Show();
};

#endif //YAP1_LIBRARY_H
