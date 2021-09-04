#include <iostream>
#include "workshop.h"

using namespace std;

int main() {
	system("chcp 1251"); // ��� ����, ����� �� ������� ���� ���������

	Workshop first; // ����������� ��� ����������
	Workshop second("���", "������� ������", 5928); // ����������� � �����������
	Workshop third = first; // ����������� ������������ ������� �������
	Workshop group[3] = { Workshop(), Workshop("������", "������", 7), first }; // ����������� ������, ������ ���� ��� ������������. ������������
	Workshop* dynamic_group; // ������������ ������ + ���������
	dynamic_group = new Workshop[2];
	dynamic_group[0].set("��������", "�������", 19); // ���������� � ������ ����� ������
	dynamic_group[1].setAmount(5); // ��������� � ������ �� �����������
	dynamic_group[1].setBoss("�������");
	dynamic_group[1].setName("�������");
	void (Workshop:: * secret)(); // ��������� �� �������-����������
	secret = &Workshop::secret;

	cout << "�������� ���� �1 - " << first.getName() << endl;
	first.setName("��������"); // ��������� �������� ����
	cout << "�������� ���� �1 - " << first.getName() << endl;

	cout << "��������� ���� �2 - " << second.getBoss() << endl;
	second.setBoss("�������"); // ��������� ����������
	cout << "��������� ���� �2 - " << second.getBoss() << endl;

	cout << "���������� ������� � ���� �3 - " << third.getAmount() << endl;
	third.setAmount(16); // ��������� ���������� �������
	cout << "���������� ������� � ���� �3 - " << third.getAmount() << endl;

	group[0].show();
	group[0].set("Name", "Boss", 100); // ��������� ����� ����� set
	group[0].show();

	dynamic_group[1].show();
	(dynamic_group[1].*secret)(); // ������ ������� :)
	dynamic_group[1].show();

	system("pause");

	delete[] dynamic_group; // ������� ������������ ������ dynamic_group
}