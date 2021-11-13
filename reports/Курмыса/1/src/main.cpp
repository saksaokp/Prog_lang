#include <iostream>
#include "workshop.h"

using namespace std;

int main() {
	Workshop first; // constructor without params
	Workshop second("Workshop", "Zubenko Mikhail", 5928); //constructor with params
	Workshop third = first; // copying constructor
	Workshop group[3] = { Workshop(), Workshop("Second", "Belyaev", 7), first }; // sttaic array with all three types of contrsuctors
	Workshop* dynamic_group; // dynamic array
	dynamic_group = new Workshop[2];
	dynamic_group[0].set("Steel", "Golubev", 19); // adding all fields together
	dynamic_group[1].setAmount(5); // adding fields by one
	dynamic_group[1].setBoss("Dolubev");
	dynamic_group[1].setName("Piping");
	void (Workshop:: *secret)(); // pointer to function-component
	secret = &Workshop::secret;

	cout << "The name of workshop No. 1 is " << first.getName() << endl;
	first.setName("Concrete"); // setter of Name
	cout << "The name of workshop No. 1 is " << first.getName() << endl;

	cout << "The boss of workshop No. 2 is " << second.getBoss() << endl;
	second.setBoss("Kamyshov"); // setter of Boss
	cout << "The boss of workshop No. 2 is " << second.getBoss() << endl;

	cout << "The amount of workers in workshop No. 3 is " << third.getAmount() << endl;
	third.setAmount(16); // setter of amount
	cout << "The amount of workers in workshop No. 3 is " << third.getAmount() << endl;

	group[0].show();
	group[0].set("Name", "Boss", 100); // setter of all three fields
	group[0].show();

	dynamic_group[1].show();
	(dynamic_group[1].*secret)(); // calling a secret function
	dynamic_group[1].show();

	system("pause");

	delete[] dynamic_group; // free dynamic memory of dynamic_group
}
