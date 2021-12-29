#ifndef WORKSHOP_H
#define WORKSHOP_H

const int NAME_LENGTH = 50; // constant for amount of chars in string

class Workshop {
	char name[NAME_LENGTH];
	char boss[NAME_LENGTH];
	int amount;
public:
	Workshop(); // constructor without params
	Workshop(const char*, const char*, int); // constructor with params
	Workshop(const Workshop&); // copying constructor
	~Workshop(); // destructor
	const char* getName(); // getting field
	const char* getBoss();
	int getAmount();
	void setName(const char*); // setting field
	void setBoss(const char*);
	void setAmount(int);
	void set(const char*, const char*, int); // setting all fields
	void show(); // getting all three fields
	void secret(); // secret function (used for pointer for function)
};

#endif
