#ifndef UNTITLED1_METROPOLIS_H
#define UNTITLED1_METROPOLIS_H
#include "town.h"

class metropolis : public town {
protected:
    float gdp;
    static metropolis *head;
    metropolis *next;
public:
    metropolis();
    metropolis(metropolis &);
    metropolis(char *, float, int, int, float);
    void Show() override;
    void Add() override;
    void setGdp(float gdp);
    static void Show_list();
    ~metropolis();
};

#endif
