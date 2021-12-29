#include "figure.h"

FiguresArray::FiguresArray() : figures(nullptr), count(0) {}

void FiguresArray::AddBack(Figure* figure) {
	count++;
	Figure** tempFigures = figures;
	figures = new Figure * [count];
	for (int i = 0; i < count - 1; i++) {
		figures[i] = tempFigures[i];
	}
	figures[count - 1] = figure;
	delete[] tempFigures;
}

void FiguresArray::Show() {
	cout << "Figures:" << endl;
	for (int i = 0; i < count; i++) {
		figures[i]->Show();
	}
}

Figure* FiguresArray::operator[](int i)
{
	if (i < 0 || i >= count)
		throw - 1;
	return figures[i];
}