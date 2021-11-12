#include "exam.h"


Exam::Exam() : name("NoName"), date(0), score(0){
    cout << "\nСоздание без параметров - (" << name << ", " << date << ", " << score << ")";
}

Exam::Exam(string name, int date, int score) : name(name), date(date), score(score){
    cout << "\nСоздание с параметрами - (" << name << ", " << date << ", " << score << ")";
}

Exam::Exam(const Exam& exam) : name(exam.name), date(exam.date), score(exam.score){
    cout << "\nСоздание с помощью копирования (" <<
        name << ", " << date << ", " << score << ")";
}

Exam::~Exam() { cout << "\nУдаление (" << name << ", " << date << ", " << score << ")"; }

void Exam::Print() const { cout << '(' << name << ", " << date << ", " << score << ")"; }

void Exam::SetName(string _name) { name = _name;}
string Exam::GetName() const { return name; }

void Exam::SetDate(int _date) { date = _date; }
int Exam::GetDate() const { return date; }

void Exam::SetScore(int _score) { score = _score; }
int Exam::GetScore() const { return score; }
