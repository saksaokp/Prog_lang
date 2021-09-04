#ifndef WORKSHOP_H
#define WORKSHOP_H

const int NAME_LENGTH = 50;

class Workshop {
	char name[NAME_LENGTH];
	char boss[NAME_LENGTH];
	int amount;
public:
	Workshop();
	Workshop(const char*, const char*, int);
	Workshop(const Workshop&);
	~Workshop();
	const char* getName();
	const char* getBoss();
	int getAmount();
	void setName(const char*);
	void setBoss(const char*);
	void setAmount(int);
	void set(const char*, const char*, int);
	void show();
	void secret();
};

#endif