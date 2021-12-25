#ifndef CLASSES_H
#define CLASSES_H

using namespace std;

class Document { // класс Документ
  public:
    Document();
    Document(string, string);
    virtual ~Document(); // так как есть виртуальные функции, то и деструктор должен быть виртуальным
    virtual void show_item() = 0; // чистая виртуальная функция для дочерних классов
    void add(); // функция добавления элементов в список
    void del(); // удаление элементов из списка (при деструкторе)
    static void show_list(); // для вывода списка элементов
  protected:
    string date; // дата создания
    string organisation; // организация, указанная в документе
    static int index; // порядковый номер документа в списке
    static int document_count; // статический элемент - кол-во документов
    static Document **documents; // список документов
};

class Receipt: public Document { // класс Квитанция
  public:
    Receipt();
    Receipt(string, string, string, string, int);
    ~Receipt();
    void show_item() override; // перезаписываем ЧВ-функцию из родительского в дочерний класс
  protected:
    string sender; // отправитель денег или иных ценностей
    string receiver; // получатель денег или иных ценностей
    int cost; // стоимость денег или иных ценностей
    static int receipt_count; // кол-во квитанций
};

class Invoice: public Document { // класс Накладная
  public:
    Invoice();
    Invoice(string, string, string, string, string);
    ~Invoice();
    void show_item() override;
  protected:
    string goods; // перевозимый товар, его описание
    string provider; // поставщик товара
    string date_of_delivery; // дата доставки товара
    static int invoice_count; // кол-во накладных
};

class Check: public Document { // Класс Чек
  public:
    Check();
    Check(string, string, string, string, double);
    ~Check();
    void show_item() override;
  protected:
    string payee; // чекодержатель
    string drawer; // чекодатель
    double amount; // цена, указанная в чеке
    static int check_count;
};

#endif
