#include <iostream>
using namespace std;


class SaleItem {
protected:
    const char *name;
    float price;

public:
    static int count;
    static SaleItem **items;

    SaleItem(const char *name, float price) : name(name), price(price) {
        add();
        cout << "Created SaleItem \"" << name << "\"\n";
    }

    virtual void print() {
        cout << "SaleItem  name: \"" << name << "\", price: " << price << "\n";
    }

    virtual void add() final {
        SaleItem** temp = items;
        items = new SaleItem* [count + 1];
        for(int i = 0; i < count; i++)
            items[i] = temp[i];
        items[count] = this;
        count++;
    }

    static void showItems() {
        for(int i=0; i<count; i++)
            items[i]->print();
    }


};


class Toy : SaleItem {

};


class Product : SaleItem {

};


class MilkProduct : Product {

};

int SaleItem::count = 0;
SaleItem **SaleItem::items = nullptr;


int main() {
    SaleItem phone("phone", 700);
    SaleItem pen("pen", 1);
    SaleItem pencil("pencil", 0.80);
    SaleItem::showItems();

}