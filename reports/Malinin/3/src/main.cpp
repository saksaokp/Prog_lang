#include <iostream>
#include <vector>
#include "number.h"
#include "array.h"


using namespace std;

int Number::numbers = 0;
int Integer::integers = 0;
int Real::reals = 0;
int Complex::complexes = 0;

bool is_valid(float a, float f = 0) {
    return (a == int(a)) && (f == int(f));
}

int main() {
    cout << "12 BapuaHT \n\n";

    Integer f1;
    Integer f2(59);
    Real f3;
    Real f4(8, 91);
    Complex f5;
    Complex f6(16, 43, 6);

    cout << "OPERATCIA ==\n";
    cout << "Number f1 u f1" << (f1 == f1 ?  " " : " ne ") << "ravno\n";
    cout << "Number f1 u f6" << (f1 == f6 ? " " : " ne ") << "ravno\n";

    cout << "\nOperatcia !=\n";
    cout << "Number f5 u f2" << (f5 != f2 ? " ne " : " ") << "Ravno\n";
    cout << "Number f6 u f6" << (f6 != f6 ? " ne " : " ") << "Ravno\n";

    Array numbers;
    numbers.push_back(&f1);
    numbers.push_back(&f2);
    numbers.push_back(&f3);
    numbers.push_back(&f4);
    numbers.push_back(&f5);
    numbers.push_back(&f6);

    Array arr;

    while (true) {
        cout << "0 - Exit\n1 - Sozd i dobavl v massiv\n2 - Dobavl sush number v massiv\n3 - Vstavka sush  v massiv\n4 - Usechenie\n5 - Delete\n6 - Vivod vseh elementov\n";
        int choice;
        cin >> choice;
        if (choice == 0) {
            cout << "EXIT...\n";
            break;
        }
        else if (choice == 1) {
            cout << "0 - Exit iz function\n1 - Cree number full\n2 - Cree VESH number\n3 - Cree complex number\n";
            int choice_2;
            cin >> choice_2;
            if (choice_2 == 0) {
                cout << "Exit ix function...\n";
                continue;
            }
            else if (choice_2 == 1) {
                cout << "Vvedite celyu chast: ";
                float a;
                cin >> a;
                if (is_valid(a)) {
                    arr.push_back(new Integer(a));
                }
                else {
                    cout << "celaya chast doljna bit celoy!\n";
                }
            }
            else if (choice_2 == 2) {
                cout << "Vvedite celyu chast: ";
                float a;
                cin >> a;
                cout << "Vvedite vesh chast: ";
                float f;
                cin >> f;
                if (is_valid(a, f)) {
                    arr.push_back(new Real(a, f));
                }
                else {
                    cout << "celaya chast i vesh doljna bit celoy!";
                }
            }
            else if (choice_2 == 3) {
                cout << "Vvedite celyu chast: ";
                float a;
                cin >> a;
                cout << "Vvedite vesh chast: ";
                float f;
                cin >> f;
                if (is_valid(a, f)) {
                    cout << "Vvedite comlex chast: ";
                    float i;
                    cin >> i;
                    arr.push_back(new Complex(a, f, i));
                }
                else {
                    cout << "celaya chast i vesh doljna bit celoy!!\n";
                }
            }
            else {
                cout << "nekkorektnoe znachenie!\n";
            }
        }
        else if (choice == 2) {
            cout << "vvedite index (ot 0 do 5), kotoroe hotite dobavit: ";
            int index;
            cin >> index;
            arr.push_back(numbers[index]);
        }
        else if (choice == 3) {
            if (arr.len() == 0) {
                cout << "pust!\n";
            }
            else {
                cout << "vvedite index (ot 0 do 5), kotoroe hotite dobavit: ";
                int index;
                cin >> index;
                cout << "vvedite poziciyu posle cotoroy hotite dobavit(ot 0 do " << arr.len() - 1 << "): ";
                int index_after;
                cin >> index_after;
                arr.insert(numbers[index], index_after);
            }
        }
        else if (choice == 4) {
            if (arr.len() == 0) {
                cout << "Massiv pust!\n";
            }
            else {
                cout << "Vvedite 4erez probel na4alnyu . u kone4nyu ot 0 do " << arr.len() - 1 << ": ";
                int begin, end;
                cin >> begin >> end;
                arr.trunc(begin, end);
            }
        }
        else if (choice == 5) {
            arr.mid_del();
        }
        else if (choice == 6) {
            cout << "Spisok elemenov:\n";
            arr.show_arr();
        }
    }
}