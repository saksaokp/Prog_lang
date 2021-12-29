#include <iomanip>
#include "books.h"

int PrintItem::count = 0; PrintItem** PrintItem::items = nullptr;

int main() {
    setlocale(LC_ALL, "Russian"); //русский язык
    Magazine SportsMag("NBA Stars 2011", 9.99, "NBA Publishing ltd.");
    SportsMag.Add(); //добавление первого элемента в список, остальные будут добавлятся при создании
    Book CnP("Преступление и наказание", 10.59, "Ф. Достоевский"); //создание книги
    Book FnC("Отцы и дети", 5.69, "И. Тургенев"); //создание книги
    TextBook Math3("Математика", 3.33, "Министерство образования РБ", 3); //создание журнала

    PrintItem::listItems(); //вывод элементов
}
