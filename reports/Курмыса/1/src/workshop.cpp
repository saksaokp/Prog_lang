#include <iostream>
#include "workshop.h"

using namespace std;

Workshop::Workshop() {
	cout << "����������� ����������� ��� ���������� ��� ������� " << this << "...\n";
	strcpy_s(name, "���");
	strcpy_s(boss, "���������");
	amount = 0;
	cout << "����������� ��� ���������� ������ ��� ������� " << this << "\n";
}

Workshop::Workshop(const char* NAME, const char* BOSS, int AMOUNT) {
	cout << "����������� ����������� � ����������� ��� ������� " << this << "...\n";
	strcpy_s(name, NAME);
	strcpy_s(boss, BOSS);
	amount = AMOUNT;
	cout << "����������� � ����������� ������ ��� ������� " << this << "\n";
}

Workshop::Workshop(const Workshop& workshop) {
	cout << "����������� ����������� ����������� ��� ������� " << this << "...\n";
	strcpy_s(name, workshop.name);
	strcpy_s(boss, workshop.boss);
	amount = workshop.amount;
	cout << "����������� ����������� ������ ��� ������� " << this << "\n";
}

Workshop::~Workshop() {
	cout << "����������� ���������� ��� ������� " << this << "...\n";
	cout << "���������� ������ ��� ������� " << this << "\n";
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
	cout << "�������� ���� - " << name << endl;
	cout << "��������� - " << boss << endl;
	cout << "���������� ������� ���� - " << amount << endl;
}

void
Workshop::secret() {
	strcpy_s(name, "Absolute Happiness");
	strcpy_s(boss, "Nice");
	amount = 69420;
}