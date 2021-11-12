#pragma once
#include "Test.h"

class Trial :
    public virtual Test
{
private:
    static list<Trial*> _list;

protected:
    string _sponsor;

public:
    Trial(int comp, string name, string spons);

    ~Trial() override;
    void Show() override;
    void Add() override;

    static void ShowAll();
};

