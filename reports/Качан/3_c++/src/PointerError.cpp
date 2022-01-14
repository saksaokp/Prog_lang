#include "PointerError.h"
PointerError::PointerError(int *ptr) {
	Pointer = ptr;
	if (Pointer == NULL) {
		ErrorText = "Pointer Error";
	}
	else {
		ErrorText = "All done";
	}
}