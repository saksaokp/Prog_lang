#include "ErrorOverflow.h"
#include<iostream>
ErrorOverflow::ErrorOverflow(int index) {
	if (index > 10) {
		ErrorText = "Overflow";
	}
	else {
		ErrorText = "All done.";
	}
}
