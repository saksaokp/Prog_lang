#include <iostream>
#include <vector>
#include "figures.h"
#include "array.h"

using namespace std;

int Figure::figures = 0;
int Cube::cubes = 0;
int Cylinder::cylinders = 0;
int Tetrahedron::tetrahedrons = 0;

int main() {
  cout << "Написать программу, в которой описана иерархия классов: геометрические фигуры (куб, цилиндр, тетраэдр). Описать класс для хранения коллекции фигур (массива указателей на базовый класс), в котором перегрузить операцию «[ ]», а также реализовать функции подсчёта общего объема и площади поверхности. Для базового класса и его потомков перегрузить операции «==», «!=», «=». Продемонстрировать работу операторов.\n\n";

  Cube f1;
  Cube f2(10);
  Cylinder f3;
  Cylinder f4(20, 1.5);
  Tetrahedron f5;
  Tetrahedron f6(10);

  cout << "Операция ==\n";
  cout << "Фигуры f1 и f1" << (f1 == f1 ? " " : " не ") << "равны\n";
  cout << "Фигуры f1 и f6" << (f1 == f6 ? " " : " не ") << "равны\n";

  cout << "\nОперация !=\n";
  cout << "Фигуры f5 и f2" << (f5 != f2 ? " не " : " ") << "равны\n";
  cout << "Фигуры f6 и f6" << (f6 != f6 ? " не " : " ") << "равны\n";

  Array figures;
  figures.push_back(&f1);
  figures.push_back(&f2);
  figures.push_back(&f3);
  figures.push_back(&f4);
  figures.push_back(&f5);
  figures.push_back(&f6);

  Array arr;
  
  while (true) {
    cout << "0 - Выход из программы\n1 - Создание фигуры и добавление её в массив\n2 - Добавление существующей фигуры в конец массива\n3 - Вставка существующей фигуры внутрь массива\n4 - Усечение массива до некоторого интервала\n5 - Удаление среднего элемента массива\n6 - Вывести значения всех элементов\n";
    int choice;
    cin >> choice;
    if (choice == 0) {
      cout << "Производится выход из программы...\n";
      break;
    } else if (choice == 1) {
      cout << "0 - Выход из функции\n1 - Создать куб\n2 - Создать цилиндр\n3 - Создать тетраэдр\n";
      int choice_2;
      cin >> choice_2;
      if (choice_2 == 0) {
        cout << "Производится выход из функции...\n";
        continue;
      } else if (choice_2 == 1) {
        cout << "Введите длину ребра куба: ";
        int a;
        cin >> a;
        arr.push_back(new Cube(a));
      } else if (choice_2 == 2) {
        cout << "Введите длину высоты цилиндра: ";
        int a;
        cin >> a;
        cout << "Введите длину радиуса основания цилиндра: ";
        int r;
        cin >> r;
        arr.push_back(new Cylinder(a, r));
      } else if (choice_2 == 3) {
        cout << "Введите длину ребра тетраэдра: ";
        int a;
        cin >> a;
        arr.push_back(new Tetrahedron(a));
      } else {
        cout << "Некорректное значение!\n";
      }
    } else if (choice == 2) {
      cout << "Введите индекс фигуры (от 0 до 5), которую Вы хотите поместить в массив фигур: ";
      int index;
      cin >> index;
      arr.push_back(figures[index]);
    } else if (choice == 3) {
      if (arr.len() == 0) {
        cout << "Массив пуст!\n";
      }
      else {
        cout << "Введите индекс фигуры (от 0 до 5), которую Вы хотите поместить в массив фигур: ";
        int index;
        cin >> index;
        cout << "Введите позицию, после которой должна быть размещена данная фигура (от 0 до " << arr.len() - 1 << "): ";
        int index_after;
        cin >> index_after;
        arr.insert(figures[index], index_after);
      }
    } else if (choice == 4) {
      if (arr.len() == 0) {
        cout << "Массив пуст!\n";
      }
      else {
        cout << "Введите через пробел начальную и конечную точку интервала от 0 до " << arr.len() - 1 << ": ";
        int begin, end;
        cin >> begin >> end;
        arr.trunc(begin, end);
      }
    } else if (choice == 5) {
      arr.mid_del();
    } else if (choice == 6) {
      cout << "Список элементов массива:\n";
      arr.show_arr();
    }
  }
} 