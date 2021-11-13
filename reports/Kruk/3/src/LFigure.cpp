#include "LFigure.h"

LFigure::LFigure(int size) {
    this->size = size - 1;
    m_figure = new pFigure[size];
    for (int i = 0; i < size; i++)
        m_figure[i] = nullptr;
}

Figure *&LFigure::operator[](int n) {
    if (n < 0 && n > size) throw LFigure(size);
    return m_figure[n];
}

void LFigure::ins(Figure *&figure) {
    int ind;
    cout << "Введите номер вставки: ";
    cin >> ind;

    if (ind < 0 || ind > size) throw LFigure(size);
    if (m_figure[ind] && m_figure[size]) throw;
    if (m_figure[ind])
        for (int i = size - 1; i > ind; i--)
            m_figure[i] = m_figure[i - 1];
    m_figure[ind] = figure;
}

void LFigure::add(Figure *&figure) {
    if (m_figure[size]) throw LFigure(size);
    int i;
    for (i = size; i >= 0 && !m_figure[i]; i--);
    m_figure[i + 1] = figure;
}

void LFigure::truncation() {
    int ind;
    cout << "Индекс усечения: ";
    cin >> ind;

    if (ind < 0 && ind > size) throw LFigure(size);
    for (int i = ind; i < size; i++)
        m_figure[i] = nullptr;
}

void LFigure::val() {
    cout << "1. Площадь" << endl
         << "2. Периметр" << endl
         << "Выберите команду: ";
    int c, ind;
    cin >> c;
    cout << "Введите индекс элемента: ";
    cin >> ind;
    if (ind >= size) throw LFigure(size);
    if (m_figure[ind] == nullptr) throw ind;
    if (c == 1) {
        double s = m_figure[ind]->square();
        if (s > numeric_limits<double>::max()) throw 0.1;
        cout << "Площадь: " << s << endl;
    }
    if (c == 2) {
        double p = m_figure[ind]->perimeter();
        if (p > numeric_limits<double>::max()) throw 0.1;
        cout << "Периметр: " << p << endl;
    }
}

void LFigure::sum() {
    double sum = 0;
    int c;
    cout << "1. Площадь" << endl
         << "2. Периметр" << endl
         << "Выберите команду: ";
    cin >> c;
    double (Figure::*f)();

    if (c == 1)
        f = &Figure::square;
    if (c == 2)
        f = &Figure::perimeter;

    for (int i = 0; i <= size; i++)
        if (m_figure[i] != nullptr)
            sum += (m_figure[i]->*f)();

    if (sum > numeric_limits<double>::max()) throw 0.1;

    if (c == 1)
        cout << "Сумарная площадь: " << sum << endl;
    else if (c == 2)
        cout << "Сумарный периметр: " << sum << endl;
}

void LFigure::del_middle() {
    for (int i = size / 2; i < size; i++)
        m_figure[i] = m_figure[i + 1];
    m_figure[size] = nullptr;
}

void LFigure::show() {
    for (int i = 0; i <= size; i++)
        if (m_figure[i] != nullptr) {
            cout << i << endl;
            m_figure[i]->print();
            cout << endl;
        }
}

LFigure::~LFigure() {
    for (int i = 0; i <= size; i++)
        if (m_figure[i] != nullptr)
            delete m_figure[i];
    delete[] m_figure;
}