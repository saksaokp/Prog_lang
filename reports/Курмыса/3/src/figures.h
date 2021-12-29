#ifndef FIGURES_H
#define FIGURES_H

using namespace std;

class Figure { // абстрактный класс фигур
  protected:
    float a; // длина ребра фигуры (либо высота цилиндра, 
             // потому что почему бы и нет =/)
    float r; // длина радиуса окружности основания (только для цилиндра)
    string name; // название фигуры
    static int figures; // количество фигур
  public:
    Figure();
    Figure(float, float, string);
    virtual ~Figure();
    virtual const float V() const = 0; // чистая виртуальная функция объёма фигуры 
    virtual const float S() const = 0; // чистая виртуальная функция площади
                                // поверхности фигуры
    virtual const void info() const = 0; // чистая виртуальная функция вывода
                             // информации о фигуре
    bool operator ==(const Figure&); // перегрузка оператора
                                     // сравнения
    bool operator !=(const Figure&); // перегрузка оператора
                                     // антисравнения =P
    const Figure& operator =(const Figure&); // перегрузка оператора
                                             // присваивания
};

class Cube: public Figure { // класс Куб
  protected:
    static int cubes; // количество кубов
  public:
    Cube();
    Cube(float);
    ~Cube();
    const float V() const override;
    const float S() const override;
    const void info() const override;
};

class Cylinder: public Figure { // класс Цилиндр
  protected:
    static int cylinders; // количество цилиндров
  public:
    Cylinder();
    Cylinder(float, float);
    ~Cylinder();
    const float V() const override;
    const float S() const override;
    const void info() const override;
};

class Tetrahedron: public Figure { // класс Тетраэдр (правильный)
  protected:
    static int tetrahedrons; // количество тетраэдров
  public:
    Tetrahedron();
    Tetrahedron(float);
    ~Tetrahedron();
    const float V() const override;
    const float S() const override;
    const void info() const override;
};

#endif