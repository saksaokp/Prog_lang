#include <iostream>
#include "workshop.h"

using namespace std;

int main() {
	Workshop first; // конструктор без параметров
	Workshop second("Workshop", "Zubenko Mikhail", 5928); // конструктор с параметрами
	Workshop third = first; // конструктор копираования первого объекта
	Workshop group[3] = { Workshop(), Workshop("Second", "Belyaev", 7), first }; // статический массив, внутри него все вышеперечисл. конструкторы
	Workshop* dynamic_group; // динамический массив + указатель
	dynamic_group = new Workshop[2];
	dynamic_group[0].set("Steel", "Golubev", 19); // добавление в объект всего вместе
	dynamic_group[1].setAmount(5); // добавлени в объект по отдельности
	dynamic_group[1].setBoss("Dolubev");
	dynamic_group[1].setName("Piping");
	void (Workshop:: *secret)(); // указатель на функцию-компоненту
	secret = &Workshop::secret;

	cout << "The name of workshop No. 1 is " << first.getName() << endl;
	first.setName("Concrete"); // изменение названия цеха
	cout << "The name of workshop No. 1 is " << first.getName() << endl;

	cout << "The boss of workshop No. 2 is " << second.getBoss() << endl;
	second.setBoss("Kamyshov"); // изменение начальника
	cout << "The boss of workshop No. 2 is " << second.getBoss() << endl;

	cout << "The amount of workers in workshop No. 3 is " << third.getAmount() << endl;
	third.setAmount(16); // изменение количества рабочих
	cout << "The amount of workers in workshop No. 3 is " << third.getAmount() << endl;

	group[0].show();
	group[0].set("Name", "Boss", 100); // изменения всего через set
	group[0].show();

	dynamic_group[1].show();
	(dynamic_group[1].*secret)(); // тайная функция :)
	dynamic_group[1].show();

	system("pause");

	delete[] dynamic_group; // очищаем динмаический массив dynamic_group
}