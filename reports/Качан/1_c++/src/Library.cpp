#include "Library.h"

Library::Library():
    name("1_book"),
    author("A.Pushkin"),
    price(33.33)
{
    cout<<"Constructor with parameters called for: "<<name<<endl;
}

Library::Library(string Name, string Author, float Price):
    name(Name),
    author(Author),
    price(Price)
{
    cout<<"Constructor without parameters called for: "<<name<<endl;
}
Library::~Library() {
    cout << "Destructor called for: " << name << endl;
}
Library::Library(const Library&lib):
    name(lib.name),
    author(lib.author),
    price(lib.price)
{
    cout<<"Copying was there. "<<endl;
}
string Library::GetName() {
    return name;
}
string Library::GetAuthor() {
    return author;
}
float Library::GetPrice() {
    return price;
}
void Library::SetName(string Name) {
    this->name = Name;
}
void Library::SetAuthor(string Author) {
    this->author = Author;
}
void Library::SetPrice(float Price) {
    this->price = Price;
}
void Library::Show() {
    cout <<"Name: "<< name << "; Author: " << author<< "; Price: " << price<< endl;
}