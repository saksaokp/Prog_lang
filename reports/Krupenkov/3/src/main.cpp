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
            cout << "  ";
            figure->printSP();
        }
    }

    bool operator==(Figure &other) {
        return (typeid(*this) == typeid(other)) && (a == other.a) && (b == other.b) && (s() == other.s());
    }

    bool operator!=(Figure &other) {
        return !(*this == other);
    }
};


class Parallelepiped : public Figure {
protected:
    float alpha;

public:
    Parallelepiped(float a, float b, float alpha) : Figure(a, b), alpha(alpha) {
        cout << "Created Parallelepiped: a = " << a << ", b = " << b << ", alpha = " << alpha << "\n";
    }

    ~Parallelepiped() {
        cout << "Deleted Parallelepiped: a = " << a << ", b = " << b << ", alpha = " << alpha << "\n";
    }

    float s() override {
        return a * b * sin(alpha);
    }

    float p() override {
        return (a + b) * 2;
    }

    void print() override {
        cout << "Parallelepiped: a = " << a << ", b = " << b << ", alpha = " << alpha << "\n";
    }
};


class Rhombus : public Parallelepiped {
public:
    Rhombus(float a, float alpha) : Parallelepiped(a, a, alpha) {
        cout << "Created Rhombus: a = b = " << a << ", alpha = " << alpha << "\n";
    }

    ~Rhombus() {
        cout << "Deleted Rhombus: a = b = " << a << ", alpha = " << alpha << " rad\n";
    }

    void print() override {
        cout << "Rhombus: a = b = " << a << ", alpha = " << alpha << " rad\n";
    }
};


class Ellipse : public Figure {
public:
    Ellipse(float a, float b) : Figure(a, b) {
        // a, b - полуоси эллипса
        cout << "Created Ellipse: a = " << a << ", b = " << b << "\n";
    }

    ~Ellipse() {
        cout << "Deleted Ellipse: a = " << a << ", b = " << b << "\n";
    }

    float s() override {
        return PI * a * b;
    }

    float p() override {
        // return 2 * PI * sqrt((a * a + b * b) / 2);
        return float(4 * (PI * a * b + pow((a - b), 2)) / (a + b));
    }

    void print() override {
        cout << "Ellipse: a = " << a << ", b = " << b << "\n";
    }
};


list<Figure *> Figure::figures;


int main() {
    Parallelepiped pip(3, 6, PI / 3);
    Parallelepiped pip2(3, 6, PI / 2);
    Rhombus sus(2, PI / 6);
    Ellipse ell(2, 8);
    cout << '\n';
    Figure::show();
    cout << '\n';

}
