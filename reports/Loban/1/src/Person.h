#ifndef PERSON_H
#define PERSON_H


class Person {
    const char *name;
    int age;
    bool isMale;

public:
    Person();

    Person(const char *name2, int age2, bool isMale2);

    Person(Person &person);

    ~Person();

    void Print();

    void SetName(const char *name2);

    const char *GetName();

    void SetAge(int age2);

    int GetAge();

    void SetSex(bool isMale2);

    bool GetSex();
};


#endif //PERSON_H
