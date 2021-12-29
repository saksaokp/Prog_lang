#ifndef BOOKS_H
#define BOOKS_H

class PrintItem {
protected:
    const char* name;
    float price;
public:
    static int count;
    static PrintItem** items;
    PrintItem(const char* name, float price, bool isAdd = true);
    ~PrintItem();
    virtual void Print() = 0;
    virtual void Add() final;
    static void listItems();
};

class Magazine : public PrintItem {
protected: const char* publisher;
public:
    Magazine(const char* name, float price, const char* publisher);
    ~Magazine();
    void Print() override;
};

class Book : protected PrintItem {
protected: const char* author;
public:
    Book(const char* name, float price, const char* author);
    ~Book();
    void Print() override;
};

class TextBook : Book {
protected: int grade;
public:
    TextBook(const char* name, float price, const char* author, int grade);
    ~TextBook();
    void Print() override;
};

#endif 