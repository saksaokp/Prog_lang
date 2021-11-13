#ifndef CLASS_H
#define CLASS_H

#include <iostream>
#include <Windows.h>

using namespace std;

class Product {
private:
    char *name;
    int number;
    float price;

public:
    Product(); //Конструктор без параметров
    Product(char *, const int, const float); //Конструктор с параметрами
    Product(const Product &); //Конструктор копии
    ~Product(); //Деструктор класса

    char *GatName(); //Функция получения имени товара
    int GetNumber(); //Функция получения количества товара
    float GetPrice(); //Функция получения цены товара
    void Show(); //Функция для просмотра полей экземпляра
    void SetName(char *); //Функция для установки значения имени товара
    void SetNumber(int); //Функция для установки значения количества товаров
    void SetPrice(float); //Функция для установки значения цены товаров
    void Set(char *, int, float); //Функция для установки значений полей экземпляра
};
#endif