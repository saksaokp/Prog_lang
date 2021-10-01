#include <iostream>
#include <cmath>
#include <list>

using namespace std;


// Фигураы:
// Ромб, параллелипипед, эллипс


class Figure {
protected:
    float a, b;
    static list<Figure*> figures;

    void add() {
        figures.push_back(this);
    }

public:

    Figure(float a, float b) : a(a), b(b) {
        cout << "Created abstract Figure: a=" << a << ", b=" << b << "\n";
        add();
    }

    virtual float s() = 0;

    virtual float p() = 0;

    virtual void print() = 0;

//    static void show() {
//        for (auto & figure : figures) {
//            cout << figure->a;
//        }
//    }
};


class Rhombus : public Figure {
protected:
    float alpha;

public:
    Rhombus(float a, float alpha) : Figure(a, a), alpha(alpha) {
        cout << "Created Rhombus: a=b=" << a << ", alpha=" << alpha << "\n";
    }

    float s() override {
        cout << sin(alpha) << endl;
        return a * a * sin(alpha);
    }

    float p() override {
        return a * 4;
    }

    void print() override {
        cout << "Rhombus: a=b=" << a << ", alpha=" << alpha << "\n";
    }
};

int main() {
    const float PI = 3.141592653589793;
    Rhombus r(2, PI / 6);
    cout << r.s() << ' ' << r.p();
//    Figure::show();

}