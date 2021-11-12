#include <iostream>
#include "FuncCollection.h"
#include "Function.h"
#include "Cos.h"
#include "Sin.h"
#include "Tan.h"

using namespace std;

int menu();
void demonstration();

int main()
{
    int command;
    FuncCollection collection;

    while (true)
    {
        command = menu(); 
        float x;
        int index;
        switch (command)
        {
        case 0:
            return 0;
        case 1: // cos
            cout << "X: " << endl;
            cin >> x;

            collection.push(Cos(x));
            break;
        case 2: // sin
            cout << "X: " << endl;
            cin >> x;

            collection.push(Sin(x));
            break;
        case 3: // tan
            cout << "X: " << endl;
            cin >> x;

            collection.push(Tan(x));
            break;
        case 4: // show
            collection.display();
            system("pause");
            break;
        case 5: // remove
            collection.display();

            cout << "Index: " << endl;
            cin >> index;

            collection.remove(index);
            collection.display();

            system("pause");
            break;
        case 6: // demo
            demonstration();
            system("pause");
            break;
        default:
            cout << "Not implemented" << endl;
            system("pause");
            break;
        }

        system("cls");
    }
    
}

int menu()
{
    cout << "Menu: " << endl;
    cout << "1. Add Cos in collection" << endl;
    cout << "2. Add Sin in collection" << endl;
    cout << "3. Add Tan in collection" << endl;
    cout << "4. Show collection values" << endl;
    cout << "5. Remove from collection" << endl;
    cout << "6. Demonstration" << endl;
    cout << "0. Exit" << endl;

    int command = 0;
    cin >> command;
    return command;
}

void demonstration()
{
    FuncCollection collection;
    Function cos = Cos(2);
    Function sin = Sin(2);
    Function tan = Tan(2);

    collection.push(cos);
    collection.push(sin);
    collection.push(tan);

    cout << "Values: " << endl;
    for (size_t i = 0; i < collection.length(); i++)
    {
        cout << collection[i].value << endl;
    }

    bool b1 = cos == sin;
    Function f = sin / cos;
    bool b2 = f == tan;

    cout << "cos == sin: " << b1 << endl;
    cout << "tg = sin/cos: " << b2 << endl;
}