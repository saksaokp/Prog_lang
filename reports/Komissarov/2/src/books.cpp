#include <iostream>
#include "books.h"
using namespace std;


PrintItem::PrintItem(const char* name, float price, bool isAdd) :
    name(name), price(price) {    
    if (isAdd) Add();
    cout << "Создан PrintItem \"" << name << "\"\n";
}
PrintItem::~PrintItem() { cout << "Удалён PrintItem \"" << name << "\"\n"; }
void PrintItem::Add() {
    PrintItem** temp = items;
    items = new PrintItem * [count + 1];
    for (int i = 0; i < count; i++) items[i] = temp[i];
    items[count] = this; count++;
}
void PrintItem::listItems() {
    cout << "\n=========================================\n";
    for (int i = 0; i < count; i++) items[i]->Print();
    cout << "=========================================\n" << endl;
}

Magazine::Magazine(const char* name, float price, const char* publisher) : PrintItem(name, price, false), publisher(publisher) { cout << "Создан журнал \"" << name << "\"\n"; }
Magazine::~Magazine() { cout << "Удалён журнал \"" << name << "\"\n"; }
void Magazine::Print() { cout << "Журнал с названием: \"" << name << "\", ценой: " << price << ", издателем: " << publisher << "\n"; }

Book::Book(const char* name, float price, const char* author) : PrintItem(name, price, true), author(author) {  cout << "Создана книга \"" << name << "\"\n"; }
Book::~Book() { cout << "Удалена книга \"" << name << "\"\n"; }
void Book::Print() { cout << "Книга с названием: \"" << name << "\", ценой: " << price << ", автором: " << author << "\n"; }

TextBook::TextBook(const char* name, float price, const char* author, int grade) : Book(name, price, author), grade(grade) {    cout << "Создан учебник \"" << name << "\"\n"; }
TextBook::~TextBook() { cout << "Удалён учебник \"" << name << "\"\n"; }
void TextBook::Print() { cout << "Учебник с названием: \"" << name << "\", ценой: " << price << ", автором: " << author << ", класс: " << grade << "\n"; }
