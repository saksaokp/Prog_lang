#include <iostream>
#include <cmath>
#include <list>

using namespace std;
const float PI = 3.141592653589793;


// Фигураы:
// Ромб, параллелипипед, эллипс


class Figure {
protected:
    float a, b;
    static list<Figure *> figures;

public:
    Figure(float a, float b) : a(a), b(b) {
        figures.push_back(this);
    }


    virtual float s() const = 0;

    virtual float p() const = 0;

    virtual void print() const = 0;

    virtual void printSP() const final {
        cout << "S = " << s() << ", P = " << p() << "\n";
    }

    static void show() {
        for (auto &figure : figures) {
            figure->print();
            cout << "  ";
            figure->printSP();
            cout << "\n";
        }
    }

    bool operator==(const Figure &other) {
        return (typeid(*this) == typeid(other)) && (a == other.a) && (b == other.b) && (s() == other.s());
    }

    bool operator!=(const Figure &other) {
        return !(*this == other);
    }

    Figure &operator=(const Figure &other) {
        return *this;
    }

};


class Parallelepiped : public Figure {
protected:
    float alpha;

public:
    Parallelepiped(float a, float b, float alpha) : Figure(a, b), alpha(alpha) {}

    float s() const override {
        return a * b * sin(alpha);
    }

    float p() const override {
        return (a + b) * 2;
    }

    void print() const override {
        cout << "Parallelepiped: a = " << a << ", b = " << b << ", alpha = " << alpha << "\n";
    }
};


class Rhombus : public Parallelepiped {
public:
    Rhombus(float a, float alpha) : Parallelepiped(a, a, alpha) {}

    void print() const override {
        cout << "Rhombus: a = b = " << a << ", alpha = " << alpha << " rad\n";
    }
};


class Ellipse : public Figure {
public:
    Ellipse(float a, float b) : Figure(a, b) {}

    float s() const override {
        return PI * a * b;
    }

    float p() const override {
        return float(4 * (PI * a * b + pow((a - b), 2)) / (a + b));
    }

    void print() const override {
        cout << "Ellipse: a = " << a << ", b = " << b << "\n";
    }
};


class FiguresList {
    FiguresList *next;
    FiguresList *last;
    Figure *self;

public:
    FiguresList() : next(nullptr), last(nullptr), self(nullptr) {}

    void add(Figure *figure) {
        if (last == nullptr) {
            self = figure;
            last = this;
        } else {
            last->next = new FiguresList;
            last = last->next;
            last->self = figure;
        }
    }

    void print() const {
        if (last != nullptr) {
            self->print();
            const FiguresList *ptr = this;
            while (ptr->next != nullptr) {
                ptr = ptr->next;
                ptr->self->print();
            }
        }
    }

    Figure &operator[](int x) {
        FiguresList *ptr = this;
        for (int i = 0; i < x; i++) {
            ptr = ptr->next;
        }
        return *ptr->self;
    }
};

list<Figure *> Figure::figures;


int main() {
    Parallelepiped pip(3, 6, PI / 3);
    Rhombus sus(2, PI / 6);
    Ellipse ell(2, 8);

    Figure::show();

    FiguresList figures;
    figures.add(&pip);
    figures.add(&sus);
    figures.add(&ell);
    figures[0] = figures[1];
    figures.print();

}
