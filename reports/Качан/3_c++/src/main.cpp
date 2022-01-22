#include <iostream>
#include "ArrayError.h"
#include "PointerError.h"
#include "ErrorIndex.h"
#include "ErrorInList.h"
#include "ErrorOverflow.h"
#include "all_errors.h"
int main() {
    int* arr = new int[10];
    for (int i = 0; i < 10; i++) {
        arr[i] = 1;
    }
    
    ArrayError a = ArrayError();
    cout << a.ErrorText << endl;
    
   
    int* testptr = &arr[3];
    PointerError pe = PointerError(testptr);
    PointerError pe2 = pe;
    bool check = pe == pe2;
    cout << "Result: " << check << endl;
    cout << "Pointer error: " << endl;
    cout << pe.ErrorText << endl;
    int index = 6;
    ErrorIndex ei = ErrorIndex(index);
    ErrorIndex ei2 = ErrorIndex(index);
    bool check1 = ei == ei2;
    cout << "Result: " << check1 << endl;
    cout << "Index error:" << endl;
    cout << ei.ErrorText << endl;
    int value = -10;
    ErrorInList eil = ErrorInList(value);
    cout << "Error in list: " << endl;
    cout << eil.ErrorText << endl;
    ErrorOverflow eo = ErrorOverflow(index);
    cout << "Overflow error: " << endl;
    cout << eo.ErrorText << endl;
    
    cout << "All errors: " << endl;
    ErrorArray ea;
    ea.AddToList(&a);
    ea.AddToList(&pe);
    ea.AddToList(&ei);
    ea.AddToList(&eil);
    ea.AddToList(&eo);
    ea.PrintArray();

    

    
    return 0;
}