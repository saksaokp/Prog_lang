#pragma once
#ifndef ARRAY_H
#define ARRAY_H

class Array {
protected:
    const Number** arr;
    int count;
public:
    Array();
    ~Array();
    int len() const;
    void show_arr();
    void push_back(const Number*);
    void insert(const Number*, int);
    void trunc(int, int);
    void mid_del();
    const Number* operator [](int);
};

#endif
