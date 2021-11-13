#pragma once
#include "Test.h"
#include <list>

class Exam :
    public Test
{
private:
    static list<Exam*> _list;

protected:
    string _subject;

public:
    Exam(int compecity, string name, string subject);
    
    ~Exam() override;
    void Show() override;
    void Add() override;

    static void ShowAll();
};

