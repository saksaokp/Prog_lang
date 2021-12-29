#include <iostream>
#include "workshop.h"

using namespace std;

Workshop::Workshop() {
	cout << "Executing a constructor without any parameters for object " << this << "...\n";
	strcpy_s(name, "Name");
	strcpy_s(boss, "Boss");
	amount = 0;
	cout << "A constructor without any parameters was executed for object " << this << "\n";
}

Workshop::Workshop(const char* NAME, const char* BOSS, int AMOUNT) {
	cout << "Executing a constructor with parameters for object " << this << "...\n";
	strcpy_s(name, NAME);
	strcpy_s(boss, BOSS);
	amount = AMOUNT;
	cout << "A constructor with parameters was executed for object " << this << "\n";
}

Workshop::Workshop(const Workshop& workshop) {
	cout << "Executing a copying constructor for object " << this << "...\n";
	strcpy_s(name, workshop.name);
	strcpy_s(boss, workshop.boss);
	amount = workshop.amount;
	cout << "A copying constructor was executed for object " << this << "\n";
}

Workshop::~Workshop() {
	cout << "Executing a destructor for object " << this << "...\n";
	cout << "A destructor was executed for object " << this << "\n";
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
	cout << "Workshop's name is " << name << endl;
	cout << "The boss is " << boss << endl;
	cout << "The amount of workers is " << amount << endl;
}

void
Workshop::secret() {
	strcpy_s(name, "Absolute Happiness");
	strcpy_s(boss, "Nice");
	amount = 69420;
}
