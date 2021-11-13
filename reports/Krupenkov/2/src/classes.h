#ifndef INC_2_CLASSES_H
#define INC_2_CLASSES_H


class SaleItem {
protected:
    const char *name;
    float price;

public:
    static int count;
    static SaleItem **items;

    SaleItem(const char *name, float price, bool isAdd=true);

    ~SaleItem();

    virtual void print() = 0;

    virtual void add() final;

    static void showItems();
};


class Toy : public SaleItem {
protected:
    int min_age;

public:
    Toy(const char *name, float price, int min_age);

    ~Toy();

    void print() override;
};


class Product : protected SaleItem {
protected:
    bool isAlcoholic;

public:
    Product(const char *name, float price, int isAlcoholic);

    ~Product();

    void print() override;
};


class MilkProduct : Product {
protected:
    float fatness;

public:
    MilkProduct(const char *name, float price, int isAlcoholic, float fatness);

    ~MilkProduct();

    void print() override;
};


#endif //INC_2_CLASSES_H
