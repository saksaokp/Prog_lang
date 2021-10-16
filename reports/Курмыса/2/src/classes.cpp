#include <iostream>
#include <cstring>
#include "classes.h"

using namespace std;

// конструктор по умолчанию для класса Document
Document::Document() {
  date = "1 января 1970";
  organisation = "Feel Good Inc.";
  add();
  cout << "Создан объект класса Document номер " << ++document_count << " через конструктор по умолчанию.\n";
}

// конструктор с параметрами для класса Document
Document::Document(string date, string organisation):
date(date), organisation(organisation) {
  add();
  cout << "Создан объект класса Document номер " << ++document_count << " через конструктор с параметрами.\n";
}

// деструктор для класса Document
Document::~Document() {
  del();
  cout << "Уничтожен объект класса Document номер " << document_count-- << ".\n";
}

// добавление нового элемента в список (при конструкторе или явном вызове)
void
Document::add() {
  Document **temp = documents;
  documents = new Document* [index + 1];
  for (int i = 0; i < index; i++) documents[i] = temp[i];
  documents[index] = this;
  index++;
}

// удаление последнего элемента из списка (при деструкторе)
void
Document::del() {
  Document **temp = documents;
  documents = new Document* [index];
  for (int i = 0; i < index - 1; i++) documents[i] = temp[i];
  index--;
}

// показ списка элементов документов
void
Document::show_list() {
  cout << "\nСписок всех документов:\n";
  for (int i = 0; i < index; i++) documents[i]->show_item();
}

// конструктор по умолчанию для класса Receipt
Receipt::Receipt(): 
Document("1 января 1970 г.", "Feel Good Inc.") {
  sender = "Иванов И.И.";
  receiver = "Сидоров С.С.";
  cost = 150;
  cout << "Создан объект класса Receipt номер " << ++receipt_count << " через конструктор по умолчанию.\n";
}

// конструктор с параметрами для класса Receipt
Receipt::Receipt(string date, string organisation, string sender, string receiver, int cost):
Document(date, organisation), sender(sender), receiver(receiver), cost(cost) {
  cout << "Создан объект класса Receipt номер " << ++receipt_count << " через конструктор с параметрами.\n";
}

// деструктор для класса Receipt
Receipt::~Receipt() {
  cout << "Уничтожен объект класса Receipt номер " << receipt_count-- << ".\n";
}

// вывод информации для объекта класса Receipt
void
Receipt::show_item() {
  cout << "Квитанция:" << endl;
  cout << "Дата: " << this->date << endl;
  cout << "Организация: " << this->organisation << endl;
  cout << "Отправитель: " << this->sender << endl;
  cout << "Получитель: " << this->receiver << endl;
  cout << "Стоимость: " << this->cost << endl << endl;
}

// конструктор по умолчанию для класса Invoice
Invoice::Invoice():
Document("1 января 1970 г.", "Feel Good Inc.") {
  goods = "Мясо, картошка, киви, репчатый лук, оливье";
  provider = "Маменко И.В.";
  date_of_delivery = "8 сентября 2008 г.";
  cout << "Создан объект класса Invoice номер " << ++invoice_count << " через конструктор по умолчанию.\n";
}

// конструктор с параметрами для класса Invoice
Invoice::Invoice(string date, string organisation, string goods, string provider, string date_of_delivery):
Document(date, organisation), goods(goods), provider(provider), date_of_delivery(date_of_delivery) {
  cout << "Создан объект клааса Invoice номер " << ++invoice_count << " через конструктор с параметрами.\n";
}

// деструктор для класса Invoice
Invoice::~Invoice() {
  cout << "Уничтожен объект класса Invoice номер " << invoice_count-- << ".\n";
}

// вывод информации для объекта класса Invoice
void
Invoice::show_item() {
  cout << "Накладная:" << endl;
  cout << "Дата: " << this->date << endl;
  cout << "Огранизация: " << this->organisation << endl;
  cout << "Товары: " << this->goods << endl;
  cout << "Поставщик: " << this->provider << endl;
  cout << "Дата поставки: " << this->date_of_delivery << endl << endl;
}

// конструктор по умолчанию для класса Check
Check::Check():
Document("1 января 1970 г.", "Feel Good Inc.") {
  payee = "Максимова О.Г.";
  drawer = "Дементьева Т.Г.";
  amount = 288.20;
  cout << "Создан объект класса Check номер " << ++check_count << " через конструктор по умолчанию.\n";
}

// конструктор с параметрами для класса Check
Check::Check(string date, string organisation, string payee, string drawer, double amount):
Document(date, organisation), payee(payee), drawer(drawer), amount(amount) {
  cout << "Создан объект класса Check номер " << ++check_count << " через конструктор с параметрами.\n";
}

// деструктор для класса Check
Check::~Check() {
  cout << "Унчитожен объект класса Check номер " << check_count-- << ".\n";
}

// вывод информации для объекта класса Check
void
Check::show_item() {
  cout << "Чек:" << endl;
  cout << "Дата: " << this->date << endl;
  cout << "Огранизация: " << this->organisation << endl;
  cout << "Чекодержтель: " << this->payee << endl;
  cout << "Чекодатель: " << this->drawer << endl;
  cout << "Сумма (в бел. руб.): " << this->amount << endl << endl;
}
