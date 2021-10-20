#pragma once
#include "Function.h"


class Cos :
    virtual public Function
{
public:
    Cos();
    Cos(float x);

    void setFuncValue(float x);
};

