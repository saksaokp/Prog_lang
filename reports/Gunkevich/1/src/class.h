#ifndef CLASS_H
#define CLASS_H
class resorces
{
private:
    const char* name;
    int age;
    int rank;
public:
    resorces();
    resorces(const char* n, int a, int g);
    resorces(const resorces& s);//копирующий конструктор
    ~resorces();
    void set(const char* n, int a, int g);//установка полей данных
    void print();//просмотр полей данных
};
#endif