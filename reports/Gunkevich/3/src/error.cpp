#include "error.h"
IndexError::IndexError(const char *message) {
    this->message = _strdup(message);
}
IndexError::~IndexError() {
    delete this->message;
}
char *IndexError::get_message() {
    return message;
}
