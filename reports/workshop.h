#ifndef WORKSHOP_H
#define WORKSHOP_H

const int NAME_LENGTH = 50; // константа для строковых величин

class Workshop {
	char name[NAME_LENGTH];
	char boss[NAME_LENGTH];
	int amount;
public:
	Workshop(); // конструктор без аргументов
	Workshop(const char*, const char*, int); // конструктор с аргументами
	Workshop(const Workshop&); // конструктор копирования
	~Workshop(); // деструктор
	const char* getName(); // получение того или иного поля
	const char* getBoss();
	int getAmount();
	void setName(const char*); // замена того или иного поля на аргумент функции
	void setBoss(const char*);
	void setAmount(int);
	void set(const char*, const char*, int); // замена всех полей на аргументы функции
	void show(); // вывод всех полей форматированным способом
	void secret(); // тайная функция (для указателя на функцию)
};

#endif