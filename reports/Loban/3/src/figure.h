#pragma once
#include <iostream>
#include <math.h>

using namespace std;

class Figure
{
public:
	virtual double V() = 0;
	virtual double S() = 0;
	virtual void Show() = 0;
	void ShowVS();
	bool operator==(Figure& figure);
	bool operator!=(Figure& figure);
};


class Sphere : public Figure
{
	const double pi = 3.1415;
	double r;
public:
	Sphere(double r);

	double V() override;
	double S() override;
	void Show() override;
	Sphere& operator=(Sphere& sphere);
};

class Pyramid : public Figure
{
	double po;
protected:
	double h;
	double l;
	double so;
public:
	Pyramid(double h, double l, double po, double so);

	double V() override;
	double S() override;
	void Show() override;
	Pyramid& operator=(Pyramid& pyramid);
};

class Cone : public Pyramid
{
	const double pi = 3.1415;
	double r;
public:
	Cone(double r, double h, double l, double so);

	double S() override;
	void Show() override;
	Cone& operator=(Cone& cone);
};

class FiguresArray {
	Figure** figures;
	int count;
public:
	FiguresArray();
	void AddBack(Figure* figure);
	void Show();
	Figure* operator[](int i);
};

