#ifndef UNTITLED_ERROR_H
#define UNTITLED_ERROR_H
#include <iostream>
#include "cstring"
class IndexError {
protected:
    char *message;
public:
    IndexError(const char *message);
    ~IndexError();
    char *get_message();
};
#endif //UNTITLED_ERROR_H
