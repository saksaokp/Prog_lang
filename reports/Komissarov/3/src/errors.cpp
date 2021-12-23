#include <iostream>
#include <iostream>
#include <iomanip>
#include <string.h>
#include "errors.h"

Error::Error(std::string message) :	errMsg(message) {
	std::cout << "created error " << errMsg << std::endl;
}
Error::~Error(){}
void Error::PrintMsg() {std::cout << errMsg << std::endl;}


AccessError::AccessError(std::string message) : Error(message), accessLevelNeeded(10) {}
AccessError::~AccessError(){}

TranslateError::TranslateError(std::string message) : Error(message) {}
TranslateError::~TranslateError() {}
void TranslateError::PrintTypes() {
	std::cout << "unknown types message" << std::endl;
}

ValueTranslateError::ValueTranslateError(std::string message) : TranslateError(message) {}
ValueTranslateError::~ValueTranslateError() {}
void ValueTranslateError::PrintTypes() {
	std::cout << "value types message" << std::endl;
}

InterfaceTranslateError::InterfaceTranslateError(std::string message) : TranslateError(message) {}
InterfaceTranslateError::~InterfaceTranslateError() {}
void InterfaceTranslateError::PrintTypes() {
	std::cout << "interface types message" << std::endl;
}



ErrorArray::ErrorArray() : ptrArray(nullptr), count(0) {}
int ErrorArray::Length() const { return count; }
void ErrorArray::AddToList(Error* error) {
    if (count == 0) { count = 1;  ptrArray = new Error*;  ptrArray[0] = error; std::cout << "Added to list ( created list )"<< std::endl; }
    else {
        count++;
        auto temp = ptrArray;
        ptrArray = new Error * [count];
        for (int i = 0; i < count; i++) { ptrArray[i] = temp[i]; }
        ptrArray[count - 1] = error;
        delete[] temp;
        std::cout << "Added to list" << std::endl;
    }
}
void ErrorArray::PrintArray() const {
    std::cout << "------------\nErrorArray: \n" << std::endl;
    for (int i = 0; i < count; i++) {
        ptrArray[i]->PrintMsg();
    }
    std::cout << "------------" << std::endl;
}
void ErrorArray::operator[](int i) {
    std::cout << "errors[" << i << "]: "; ptrArray[i]->PrintMsg();
}


