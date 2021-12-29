#include <iostream>
#include <cmath>
#include "number.h"
#include "array.h"

using namespace std;

Array::Array() : arr(nullptr), count(0) {
    cout << "creet massiv 4erez constr.\n";
}

Array::~Array() {
    delete[] arr;
    cout << "delete 4erez destr.\n";
}

int
Array::len() const {
    return count;
}

void
Array::show_arr() {
    if (count == 0) {
        cout << "Pusto!\n";
    }
    else {
        for (int i = 0; i < count; i++) {
            arr[i]->info();
        }
    }
}

void
Array::push_back(const Number* number) {
    if (number != NULL) {
        if (count == 0) {
            count = 1;
            arr = new const Number * [count];
            arr[0] = number;
            cout << "Number vnytri!\n";
        }
        else {
            count++;
            auto new_arr = new const Number * [count];
            for (int i = 0; i < count - 1; i++) {
                new_arr[i] = arr[i];
            }
            new_arr[count - 1] = number;
            arr = new_arr;
            cout << "Number vnytri!\n";
        }
    }
}

void
Array::insert(const Number* number, int index) {
    if (number != NULL) {
        try {
            if (index >= count || index < 0) {
                throw "vihod za predely!\n";
            }
            count++;
            auto new_arr = new const Number * [count];
            for (int i = 0; i < index + 1; i++) {
                new_arr[i] = arr[i];
            }
            new_arr[index + 1] = number;
            for (int i = index + 1; i < count; i++) {
                new_arr[i + 1] = arr[i];
            }
            arr = new_arr;
            cout << "Number vnytri!\n";
        }
        catch (char const* s) {
            cout << s << endl;
        }
    }
}

void
Array::trunc(int begin, int end) {
    try {
        if (begin > end) {
            throw "Na4alo ne > konca!\n";
        }
        if (begin < 0 || end >= count) {
            throw "vyhod za predely!\n";
        }
        count = end - begin + 1;
        auto new_arr = new const Number * [count];
        for (int i = begin; i < end + 1; i++) {
            new_arr[i - begin] = arr[i];
        }
        arr = new_arr;
        cout << "Massiv yrezan!\n";
    }
    catch (char const* s) {
        cout << s << endl;
    }
}

void
Array::mid_del() {
    try {
        if (count == 0) {
            throw "Pusto!\n";
        }
        int del_index = count / 2;
        count--;
        auto new_arr = new const Number * [count];
        for (int i = 0; i < del_index; i++) new_arr[i] = arr[i];
        for (int i = del_index + 1; i < count + 1; i++) new_arr[i - 1] = arr[i];
        arr = new_arr;
        cout << "AVG vyrezan!\n";
    }
    catch (char const* s) {
        cout << s << endl;
    }
}

const Number*
Array::operator [](int index) {
    try {
        if (index >= count || index < -count) {
            throw "vyhod za predely!\n";
        }
        return (index >= 0) ? arr[index] : arr[count + index];
    }
    catch (char const* s) {
        cout << s << endl;
    }
}