#include "LFigure.h"

void text();

int menu();

void add_elements(Figure *&);

void comparison();


int main() {
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
    text();
    cout << "Введите размер массива: ";
    int size, c;
    cin >> size;
    system("cls");
    LFigure mas(size);
    Figure *f;
    while ((c = menu())) {
        try {
            switch (c) {
                case 1:
                    add_elements(f);
                    mas.add(f);
                    break;
                case 2:
                    comparison();
                    break;
                case 3:
                    mas.truncation();
                    break;
                case 4:
                    mas.val();
                    break;
                case 5:
                    mas.sum();
                    break;
                case 6:
                    add_elements(f);
                    mas.ins(f);
                    break;
                case 7:
                    mas.del_middle();
                    break;
                case 8:
                    mas.show();
                    break;
            }
            system("pause");
            system("cls");
        }
        catch (int) {
            cout << "\nЭлемента под таким индексом нет" << endl;
            system("pause");
            system("cls");
        }
        catch (LFigure) {
            cout << "\nВыход за пределы массива!" << endl;
            system("pause");
            system("cls");
        }
        catch (double) {
            cout << "\nСлишком большое число!" << endl;
            system("pause");
            system("cls");
        }
    }
    return 0;
}

void text() {
    cout << "Написать программу, в которой описана иерархия классов: геометрические финуры" << endl
         << "(элипс, квадрат, трапеция). Описать класс для хранения колекции финур (массива " << endl
         << "указателей на базовый класс), в котором перегрузить операцию [], а также реализовать" << endl
         << "функции полсчёта общей площади и периметра. Для базового класса и его потомков" << endl
         << "перегрущить операции < == >, < != >, < = >. Продемострировать работу операторов." << endl;
    system("pause");
    system("cls");
}

int menu() {
    int c;
    cout << "1. Добавить объект класса" << endl
         << "2. Сравнить два элемента" << endl
         << "3. Усечение массива" << endl
         << "4. Вывести площадь или периметр элемента" << endl
         << "5. Вывести сумарную площадь или периметр" << endl
         << "6. Вставка элемента" << endl
         << "7. Удаление среднего элемента" << endl
         << "8. Вывести массив" << endl
         << "0. Выход из программы" << endl;
    cout << "Выберите команду: ";
    cin >> c;
    system("cls");
    return c;
}

void add_elements(Figure *&f) {
    cout << "1. Элипс" << endl
         << "2. Квадрат" << endl
         << "3. Трапеция" << endl
         << "Выберите класс: ";
    int c;
    cin >> c;
    switch (c) {
        case 1:
            f = new Ellipses();
            break;
        case 2:
            f = new Foursquare();
            break;
        case 3:
            f = new Trapezoid();
            break;
    }
}

void comparison() {
    cout << "Выберите класс: " << endl
         << "1. Элипс" << endl
         << "2. Квадрат" << endl
         << "3. Трапеция" << endl
         << "Выберите команду: ";
    int c;
    cin >> c;
    switch (c) {
        case 1: {
            cout << "\nПервый элемент: ";
            Ellipses o1;
            cout << "\nВторой элемент: ";
            Ellipses o2;
            if (o1 == o2)
                cout << "Элипсы равны" << endl;
            if (o1 != o2)
                cout << "Элипсы не равны" << endl;
            break;
        }
        case 2: {
            cout << "\nПервый элемент: ";
            Foursquare o1;
            cout << "\nВторой элемент: ";
            Foursquare o2;
            if (o1 == o2)
                cout << "Квадраты равны" << endl;
            if (o1 != o2)
                cout << "Квадраты не равны" << endl;
            break;
        }
        case 3: {
            cout << "\nПервый элемент: ";
            Trapezoid o1;
            cout << "\nВторой элемент: ";
            Trapezoid o2;

            if (o1 == o2)
                cout << "Трапеции равны" << endl;
            if (o1 != o2)
                cout << "Трапеции не равны" << endl;
            break;
        }
    }
}
