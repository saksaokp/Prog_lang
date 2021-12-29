#ifndef ARRAY_H
#define ARRAY_H

class Array {
  protected:
    const Figure **arr; // массив указателей на фигуры
    int count; // количество элементов
  public:
    Array(); // конструктор пустого массива
    ~Array(); // деструктор
    int len() const; // функция олучения длины массива
    void show_arr(); // вывод информации об элементах
    void push_back(const Figure*); // вставка в конец
    void insert(const Figure*, int); // вставка
    void trunc(int, int); // усечение до интервала [begin, end]
    void mid_del(); // удаление из середины
    const Figure* operator [](int); // оператор "[]"
};

#endif