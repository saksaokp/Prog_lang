#ifndef INC_3_LFIGURE_H
#define INC_3_LFIGURE_H

#include "limits"
#include "Figure.h"
#include "Ellipses.h"
#include "Foursquare.h"
#include "Trapezoid.h"
#include "windows.h"

typedef Figure *pFigure;

class LFigure {
    pFigure *m_figure;
    int size;
public:
    LFigure(int);
    Figure*& operator[](int);
    void ins(Figure *&);
    void add(Figure *&);
    void val();
    void sum();
    void truncation();
    void del_middle();
    void show();
    ~LFigure();
};


#endif
