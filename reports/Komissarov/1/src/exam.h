#ifndef EXAM_H
#define EXAM_H
#include <iostream>
#include <string>
#include <string.h>
using namespace std;

class Exam {

private:
    string name;
    int date;
    int score;

public:
    Exam();
    Exam(string name, int date, int score);
    Exam(const Exam& exam);
    ~Exam();
    void Print() const;
    void SetName(string _name);
    string GetName() const;
    void SetDate(int _date);
    int GetDate() const;
    void SetScore(int _score);
    int GetScore() const;
};

#endif 
