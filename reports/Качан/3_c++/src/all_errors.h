#include<string>
#include<typeinfo>
#include "ArrayError.h"

class ErrorArray {
    ArrayError** ptrArray;  //PointerArray
    int count;  //ArrayElementCount
public:
    ErrorArray();
    int Length() const;
    void AddToList(ArrayError* error);
    void PrintArray() const;
    void operator[](int i);
};
