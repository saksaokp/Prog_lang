#include "all_errors.h"
#include<iostream>
using namespace std;
ErrorArray::ErrorArray() : ptrArray(nullptr), count(0) {}
int ErrorArray::Length() const { return count; }
void ErrorArray::AddToList(ArrayError* error) {
    if (count == 0) { 
        count = 1;  
        ptrArray = new ArrayError*;  
        ptrArray[0] = error; 
        std::cout << "Added to list ( created list )" << std::endl;
    }
    else {
        count++;
        auto temp = ptrArray;
        ptrArray = new ArrayError * [count];
        for (int i = 0; i < count; i++) { ptrArray[i] = temp[i]; }
        ptrArray[count - 1] = error;
        delete[] temp;
        cout << "Added to list" << endl;
    }
}
void ErrorArray::PrintArray() const {
    cout << "------------\nErrorArray: \n" << endl;
    for (int i = 0; i < count; i++) {
        cout << ptrArray[i]->ErrorText << endl;
    }
    cout << "------------" << endl;
}
void ErrorArray::operator[](int i) {
    cout << "errors[" << i << "]: " << endl;
    cout << ptrArray[i]->ErrorText << endl;
}