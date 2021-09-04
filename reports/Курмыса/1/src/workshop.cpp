#include <iostream>
#include "workshop.h"

using namespace std;

Workshop::Workshop() {
	cout << "Выполняется конструктор без параметров для объекта " << this << "...\n";
	strcpy_s(name, "Имя");
	strcpy_s(boss, "Начальник");
	amount = 0;
	cout << "Конструктор без параметров вызван для объекта " << this << "\n";
}

Workshop::Workshop(const char* NAME, const char* BOSS, int AMOUNT) {
	cout << "Выполняется конструктор с параметрами для объекта " << this << "...\n";
	strcpy_s(name, NAME);
	strcpy_s(boss, BOSS);
	amount = AMOUNT;
	cout << "Конструктор с параметрами вызван для объекта " << this << "\n";
}

Workshop::Workshop(const Workshop& workshop) {
	cout << "Выполняется конструктор копирования для объекта " << this << "...\n";
	strcpy_s(name, workshop.name);
	strcpy_s(boss, workshop.boss);
	amount = workshop.amount;
	cout << "Конструктор копирования вызван для объекта " << this << "\n";
}

Workshop::~Workshop() {
	cout << "Выполняется деструктор для объекта " << this << "...\n";
	cout << "Деструктор вызван для объекта " << this << "\n";
}

const char*
Workshop::getName() {
	return name;
}

void
Workshop::setName(const char* NAME) {
	strcpy_s(name, NAME);
}

const char*
Workshop::getBoss() {
	return boss;
}

void
Workshop::setBoss(const char* BOSS) {
	strcpy_s(boss, BOSS);
}

int
Workshop::getAmount() {
	return amount;
}

void
Workshop::setAmount(int AMOUNT) {
	amount = AMOUNT;
}

void
Workshop::set(const char* NAME, const char* BOSS, int AMOUNT) {
	strcpy_s(name, NAME);
	strcpy_s(boss, BOSS);
	amount = AMOUNT;
}

void
Workshop::show() {
	cout << "Название цеха - " << name << endl;
	cout << "Начальник - " << boss << endl;
	cout << "Количество рабочих цеха - " << amount << endl;
}

void
Workshop::secret() {
	strcpy_s(name, "Absolute Happiness");
	strcpy_s(boss, "Nice");
	amount = 69420;
}
