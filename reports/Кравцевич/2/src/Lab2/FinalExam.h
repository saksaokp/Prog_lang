#pragma once
#include "Exam.h"
class FinalExam :
    public Exam
{
private:
    static list<FinalExam*> _list;

protected:
    int _mark;

public:
    FinalExam(int comp, string name, string sybj, int mark);

    ~FinalExam() override;
    void Add() override;
    void Show() override;

    static void ShowAll();
};