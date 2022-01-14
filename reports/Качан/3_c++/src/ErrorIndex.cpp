#include "ErrorIndex.h"
ErrorIndex::ErrorIndex(int index) {
	Index = index;
	if (index < 0 ) {
		ErrorText = "Error while working with index.";
	}
	else {
		ErrorText = "All done.";
	}
}