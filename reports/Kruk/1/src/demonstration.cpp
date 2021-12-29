 #include "class.h"

Product Example(Product &a) {
    Product temp(a);
    temp.SetName("Чёрный хлеб");
    return temp;
}

int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    Product List1[] = {Product("Хлеб", 10, 0.79), //Выделения массива
                       Product("Батон", 5, 0.89)}; //в статической памяти
    Product *p = &List1[0]; //Объявление указателя на экземпляр класса
    p->Show(); //Использование указателя на экземпляр класса
    List1[1].Show();

    Product *List2 = new Product[2]; //Выделения массива в динамической памяти
    void (Product::*f)(char *, int, float) = &Product::Set; //Объявление указателя на функцию
    (List2[0].*f)("Конфеты", 100, 0.20); //Использование указателя на функцию
    (List2[1].*f)("Печенья", 124, 1.34); //Использование указателя на функцию
    List2[0].Show();
    List2[1].Show();

    Product Copy = Example(List1[0]);
    Copy.Show();

    delete[] List2;
}