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

    ~SaleItem() {
        cout << "Deleted SaleItem \"" << name << "\"\n";
    }

    virtual void print() = 0;

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
protected:
    int min_age;

public:
    Toy(const char *name, float price, int min_age) : SaleItem(name, price), min_age(min_age) {
        cout << "Created Toy \"" << name << "\"\n";
    }

    ~Toy() {
        cout << "Deleted Toy \"" << name << "\"\n";
    }

    void print() override {
        cout << "Toy with name: \"" << name << "\", price: " << price << ", min_age: " << min_age << "\n";
    }
};


class Product : protected SaleItem {
protected:
    bool isAlcoholic;

public:
    Product(const char *name, float price, int isAlcoholic) : SaleItem(name, price), isAlcoholic(isAlcoholic) {
        cout << "Created Product \"" << name << "\"\n";
    }

    ~Product() {
        cout << "Deleted Product \"" << name << "\"\n";
    }

    void print() override {
        cout << "Product with name: \"" << name << "\", price: " << price << ", isAlcoholic: " << isAlcoholic << "\n";
    }
};


class MilkProduct : Product{
protected:
    float fatness;

public:
    MilkProduct(const char *name, float price, int isAlcoholic, float fatness) :
    Product(name, price, isAlcoholic), fatness(fatness) {
        cout << "Created MilkProduct \"" << name << "\"\n";
    }

    ~MilkProduct() {
        cout << "Deleted MilkProduct \"" << name << "\"\n";
    }

    void print() override {
        cout << "MilkProduct with name: \"" << name << "\", price: " << price
        << ", isAlcoholic: " << isAlcoholic << ", fatness " << fatness << "\n";
    }
};


int SaleItem::count = 0;
SaleItem **SaleItem::items = nullptr;


int main() {
    Toy pony("AppleJack", 7, 0);
    Product beer("beer", 1.59, true);
    Product crisps("crisps", 3.47, false);
    MilkProduct milk("milk", 1.59, false, 3.6);

    SaleItem::showItems();
}