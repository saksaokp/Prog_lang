#include <iostream>
#include <iomanip>
#include <string.h>
#include "errors.h"
using namespace std;


int main() {
	setlocale(LC_ALL, "Russian");
	std::cout << "6. Hаписать программу, в которой описана иерархия классов: ошибка в программе («недостаточно привилегий», «ошибка преобразования», «невозможно преобразовать значение», «невозможно привести к интерфейсу»). Описать класс для хранения коллекции ошибок (массива указателей на базовый класс), в котором перегрузить операцию «[ ]». Для базового класса и его потомков перегрузить операции «==», «!=», «=». Продемонстрировать работу операторов.\n" << std::endl;

	AccessError AError("недостаточно привелегий");
	TranslateError TError1("ошибка преобразования 1");
	TranslateError TError2("ошибка преобразования 2");
	ValueTranslateError VTError("невозможно преобразовать значение");
	InterfaceTranslateError ITError("невозможно привести к интерфейсу");
	ErrorArray EA;

	EA.AddToList(&AError);
	EA.AddToList(&TError1);
	EA.AddToList(&TError2);
	EA.AddToList(&VTError);
	EA.AddToList(&ITError);
	EA.PrintArray();

	EA[2];
	EA[1];
	std::cout << (TError1 == TError2) << std::endl;
	TError1 = TError2;
	std::cout << (TError1 == TError2) << std::endl;
	return 0;
}
