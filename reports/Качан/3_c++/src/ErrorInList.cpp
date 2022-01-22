#include "ErrorInList.h"
#include<iostream>
using namespace std;
ErrorInList::ErrorInList(int value) {
	if (value<0) {
		ErrorText = "Error while working with array";
	}
	else {
		ErrorText = "All done.";
	}
}