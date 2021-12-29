#pragma once
#ifndef NUMBER_H
#define NUMBER_H

using namespace std;

class Number {
protected:
    int a; // целая часть
    int f; // вещественная часть
    float i; // комплексная часть
    string name; // наименование класса числа
    static int numbers; //
public:
    Number();
    Number(int, int, float, string);
    virtual ~Number();
    virtual const void out() const = 0;
    virtual const void info() const = 0;
    bool operator ==(const Number&);
    bool operator !=(const Number&);
    const Number& operator =(const Number&);
};

class Integer : public Number {
protected:
    static int integers;
public:
    Integer();
    Integer(int);
    ~Integer();
    const void out() const override;
    const void info() const override;
};

class Real : public Number {
protected:
    static int reals;
public:
    Real();
    Real(int, int);
    ~Real();
    const void out() const override;
    const void info() const override;
};

class Complex : public Number {
protected:
    static int complexes;
public:
    Complex();
    Complex(int, int, float);
    ~Complex();
    const void out() const override;
    const void info() const override;
};

#endif