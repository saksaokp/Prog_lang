#include <iostream>
#include "classes.h"

int Document::document_count = 0;
int Document::index = 0;
int Receipt::receipt_count = 0;
int Invoice::invoice_count = 0;
int Check::check_count = 0;
Document** Document::documents = nullptr;

int main() {
  std::system("chcp 1251"); // для того чтобы компилятор не сходил с ума
  // неявное добавление объектов в список (через конструктор)
  Receipt doc1;
  Receipt doc2("1 ноября 2001 г.", "Vitruvium", "Гордеев А.Г.", "Филатова В.А.", 846);
  
  Invoice doc3;
  Invoice doc4("29 февраля 2004 г.", "Карацинов и компания", "Трубопрокатные материалы", "Карацинов А.В.", "7 марта 2004 г.");

  Check doc5;
  Check doc6("15 сентября 2021 г.", "Белагропромбанк", "Коновалова С.В.", "Мальцева Е.Д.", 500.39);

  // явное добавление объектов в список путём вызова add()
  doc2.add();
  doc5.add();
  doc4.add();

  Document::show_list();
}
