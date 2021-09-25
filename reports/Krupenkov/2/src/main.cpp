#include "classes.h"

int SaleItem::count = 0;
SaleItem **SaleItem::items = nullptr;

int main() {
    Toy pony("AppleJack", 7, 0);
    pony.add();
    // Для остальных add используется по умолчанию в родительском классе
    Product beer("beer", 1.59, true);
    Product crisps("crisps", 3.47, false);
    MilkProduct milk("milk", 1.59, false, 3.6);

    SaleItem::showItems();
}
