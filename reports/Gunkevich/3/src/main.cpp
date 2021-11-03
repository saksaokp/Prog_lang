#include <iostream>
#include "human.h"
#include "schoolkid.h"
#include "preschooler.h"
#include "student.h"
#include "worker.h"
#include "string"
#include "HumanArray.h"
void menu(HumanArray arr);

int main() {
    setlocale(LC_ALL, "ru");

    cout << "Вариант 3." << endl
         << "Написать программу, в которой описана иерархия классов: человек («дошкольник»,«школьник», «студент», «работающий»)."
         << endl << "Описать класс для хранения коллекции людей (массива указателей на базовый класс), в котором пергрузить операцию [ ],"
         << endl <<" Для базового класса и его потомков перегрузить"
         << endl << "операции ==, !=, =. Продеманстрировать работу операторов." << endl;

    HumanArray arr(0);
    menu(arr);

    return 0;
}

void menu(HumanArray arr) {
    bool exit = false;

    while (!exit) {
        cout << "1 - add preschooler" << endl
             << "2 - add schoolkid" << endl
             << "3 - add student" << endl
             << "4 - add worker" << endl
             << "5 - Show information about a person by index" << endl
             << "6 - Show all" << endl
             << "7 - remove from the end" << endl
             << "8 - delete by index" << endl
             << "9 - compare the ages of preschoolers" << endl
             << "0 - Exit" << endl;
        try
        {
            int num;
            cin >> num;
            cout << endl;
            switch (num)
            {
                case 1:
                {
                    Preschooler *obj1 = new Preschooler("", 0);
                    obj1->Read();
                    Preschooler *obj2 = new Preschooler("", 0);
                    obj2 = obj1;

                    bool temp = false;
                    cout << "Add to the end (0) or by index (1)?";
                    cin >> temp;
                    if (temp) {
                        int index;
                        cout << "Enter the index: ";
                        cin >> index;
                        arr.add(index, obj2);
                    }
                    else {
                        arr.addToTheEnd(obj2);
                    }
                    break;
                }
                case 2:
                {
                    Schoolkid *obj = new Schoolkid("", 0);
                    obj->Read();
                    bool temp = false;
                    cout << "Add to the end (0) or by index (1)?";
                    cin >> temp;
                    if (temp) {
                        int index;
                        cout << "Enter the index: ";
                        cin >> index;
                        arr.add(index, obj);
                    }
                    else {
                        arr.addToTheEnd(obj);
                    }
                    break;
                }
                case 3:
                {
                    Student *obj = new Student("");
                    obj->Read();
                    bool temp = false;
                    cout << "Add to the end (0) or by index (1)?";
                    cin >> temp;
                    if (temp) {
                        int index;
                        cout << "Enter the index: ";
                        cin >> index;
                        arr.add(index, obj);
                    }
                    else {
                        arr.addToTheEnd(obj);
                    }
                    break;
                }
                case 4:
                {
                    Worker *obj = new Worker("");
                    obj->Read();
                    bool temp = false;
                    cout << "Add to the end (0) or by index (1)?";
                    cin >> temp;
                    if (temp) {
                        int index;
                        cout << "Enter the index: ";
                        cin >> index;
                        arr.add(index, obj);
                    }
                    else {
                        arr.addToTheEnd(obj);
                    }
                    break;
                }
                case 5:
                {
                    int index;
                    cout << "Enter the index: ";
                    cin >> index;
                    if (arr[index] != 0) {
                        arr[index]->Print();
                    }
                    break;
                }
                case 6:
                {
                    cout << "Number of people = " << arr.get_count() << endl;
                    for (int i = 0; i < arr.get_count(); i++) {
                        arr[i]->Print();
                    }
                    break;
                }
                case 7:
                {
                    arr.deleteFromTheEnd();
                    break;
                }
                case 8:
                {
                    int index;
                    cout << "Enter the index: ";
                    cin >> index;
                    arr.del(index);
                    break;
                }
                case 0:
                    exit = true;
                case 9: {
                    Preschooler obj1("", 0);
                    obj1.Read();
                    Preschooler obj2("", 0);
                    obj2.Read();
                    if (obj1 == obj2) {
                        cout << "Age equal" << endl;
                    } else if (obj1 != obj2) {
                        cout << "different age" << endl;
                    }
                    break;
                }
            }
            cout << endl;
        }
        catch (IndexError &e)
        {
            cout << "Index error: " << e.get_message() << endl;
        }
        catch (...)
        {
            cout << "Unknown error" << endl;
        }
    }
}