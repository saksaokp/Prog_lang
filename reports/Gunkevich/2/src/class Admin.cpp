#include "class Admin.h"

Admin* Admin::head = NULL;
Admin::Admin() {
	add();
}

void Admin::show() {
	cout << "Вызов виртуальной функции" << endl;
}

void Admin::add() {
	Admin* p = this;
	p->next = head;
	head = p;
}

void Admin::look_up_list() {
	Admin* p = head;
	cout << "Просмотр списка" << endl;
	while (p) {
		cout << "==============================================================" << endl;
		p->show();
		p = p->next;
	}
}

Admin::~Admin() {}