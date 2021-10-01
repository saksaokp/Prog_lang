#include <iostream>
#include <cmath>
#include <list>

using namespace std;


// Фигураы:
// Ромб, параллелипипед, эллипс


class Figure {
protected:
    float a, b;
    static list<Figure *> figures;

public:
    Figure(float a, float b) : a(a), b(b) {
        cout << "Created abstract Figure: a = " << a << ", b = " << b << "\n";
        figures.push_back(this);
    }

    ~Figure() {
        cout << "Deleted abstract Figure: a = " << a << ", b = " << b << "\n";

    }

    virtual float s() = 0;

    virtual float p() = 0;

    virtual void print() = 0;

    virtual void printSP() final {
        cout << "S = " << s() << ", P = " << p() << "\n";
    }

    static void show() {
        for (auto &figure : figures) {
            figure->print();
            figure->printSP();
        }
    }
};


class Rhombus : public Figure {
protected:
    float alpha;

public:
    Rhombus(float a, float alpha) : Figure(a, a), alpha(alpha) {
        cout << "Created Rhombus: a = b = " << a << ", alpha = " << alpha << "\n";
    }

    ~Rhombus() {
        cout << "Deleted Rhombus: a = b = " << a << ", alpha = " << alpha << " rad\n";
    }

    float s() override {
        return a * a * sin(alpha);
    }

    float p() override {
        return a * 4;
    }

    void print() override {
        cout << "Rhombus: a = b = " << a << ", alpha = " << alpha << " rad\n";
    }
};


list<Figure *> Figure::figures;


int main() {
    const float PI = 3.141592653589793;
    Rhombus r(2, PI / 6);
    Figure::show();

}