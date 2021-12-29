//
// Created by DualistOFFsetWOT on 26.12.2021.
//



#include "iostream"
#include "string"
#include "list"
using namespace std;


class Engine {//двигатель
    static list<Engine*>objects;
protected:
    int power_r;//vjoyjcnm
    float cost_t;//стоимость
public:
    Engine(int power, float cost);
    virtual ~Engine();
    static void print();
    virtual void show() = 0;
    void add();
};


class Combustion_engine : public Engine {//двигатель внутреннего сгорания
protected:
    int fuel_l;//расход топлива
public:
    Combustion_engine(int power, float cost, int fuelL);
    void show() override;
    virtual ~Combustion_engine();
};


class Diesel : public Combustion_engine {//дизель
protected:
    string transport_t;//вид транспотра
public:
    Diesel(int power, float cost, int fuel, string transport_t);
    virtual ~Diesel();
    void show() override;
};


class Turbojet_engine : public Engine {//турбореактивный двигатель
protected:
    string vendor_r; //поставщик
public:
    Turbojet_engine(int power, float cost, string vendor);
    virtual ~Turbojet_engine();
    void show() override;
};

