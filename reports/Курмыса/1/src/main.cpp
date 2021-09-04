#include <iostream>
#include "workshop.h"

using namespace std;

int main() {
	system("chcp 1251"); // для того, чтобы на консоли была кириллица

	Workshop first; // конструктор без параметров
	Workshop second("Цех", "Зубенко Михаил", 5928); // конструктор с параметрами
	Workshop third = first; // конструктор копираования первого объекта
	Workshop group[3] = { Workshop(), Workshop("Второй", "Беляев", 7), first }; // статический массив, внутри него все вышеперечисл. конструкторы
	Workshop* dynamic_group; // динамический массив + указатель
	dynamic_group = new Workshop[2];
	dynamic_group[0].set("Стальной", "Голубев", 19); // добавление в объект всего вместе
	dynamic_group[1].setAmount(5); // добавлени в объект по отдельности
	dynamic_group[1].setBoss("Долубев");
	dynamic_group[1].setName("Трубный");
	void (Workshop:: * secret)(); // указатель на функцию-компоненту
	secret = &Workshop::secret;

	cout << "Название цеха №1 - " << first.getName() << endl;
	first.setName("Бетонный"); // изменение названия цеха
	cout << "Название цеха №1 - " << first.getName() << endl;

	cout << "Начальник цеха №2 - " << second.getBoss() << endl;
	second.setBoss("Камышёв"); // изменение начальника
	cout << "Начальник цеха №2 - " << second.getBoss() << endl;

	cout << "Количество рабочих в цехе №3 - " << third.getAmount() << endl;
	third.setAmount(16); // изменение количества рабочих
	cout << "Количество рабочих в цехе №3 - " << third.getAmount() << endl;

	group[0].show();
	group[0].set("Name", "Boss", 100); // изменения всего через set
	group[0].show();

	dynamic_group[1].show();
	(dynamic_group[1].*secret)(); // тайная функция :)
	dynamic_group[1].show();

	system("pause");

	delete[] dynamic_group; // очищаем динмаический массив dynamic_group
}