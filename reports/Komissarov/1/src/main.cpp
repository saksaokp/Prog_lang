#include "exam.h"


int main() {
    setlocale(LC_ALL, "russian");
    cout << "Создание объектов класса разными способами:" << endl;
        auto* exam_noParam = new Exam;   //без параметров
        auto* exam_param = new Exam("Andrey", 2, 3);   //с параметрами
        auto* exam_copy = new Exam(*exam_param);   //копированиe
    
    cout << "\n\nДоступ к объектам через методы изменения полей: " << endl;
    cout << "\nсмена имени: ";
        exam_noParam->SetName("первый объект");
        exam_noParam->Print();

    cout << "\nсмена даты: ";
        exam_param->SetDate(9);
        exam_param->Print();

    cout << "\n\nИспользование указателя на объект(экземпляр) класса: " << endl;
        Exam* exam_ptr; //создание указателя на объект
        exam_ptr = &*exam_copy; //присвоение адреса другого объектa
    cout << "\nОбъект, до изменения его через указатель: ";   
        exam_copy->Print(); 
    cout << "\nИзменение объекта через указатель...";    
        exam_ptr->SetName("Виктор");
    cout << "\nВывод объекта через указатель: ";    
        exam_ptr->Print();
    cout << "\nВывод самого объекта: ";    
        exam_copy->Print();

    //Использование указателя на метод класса
    cout << "\n\nИспользование указателя на метод класса: " << endl;
    cout << "\nСоздание указателя на метод...";    
        void (Exam::* PrintP)() const;
    cout << "\nПрисвоение метода указателю...";    
        PrintP = &Exam::Print;
    cout << "\nВывод объекта через указатель: ";    
        (exam_copy->*PrintP)();


    cout << "\n\nУдаление объектов: \n";
        delete exam_noParam;
        delete exam_param;
        delete exam_copy;
}