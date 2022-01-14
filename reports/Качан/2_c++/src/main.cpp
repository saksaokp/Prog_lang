#include "Organization.h"
#include "Company.h"
#include "Sudos.h"
#include "Factory.h"

int main(){
    list<Organization*> organization;
    auto *firstCompany = new Company("QWERTY", 15000);
    firstCompany->set_price(10000);
    firstCompany->show();
    organization.push_back(firstCompany);

    cout<<""<<endl;
    Sudos *s1 = new Sudos("Export", 175);
    s1->set_number(150);
    cout<<"Number of ships: "<<s1->get_number()<<endl;
    organization.push_back(s1);
    std::for_each(organization.begin(), organization.end(), [](Organization* organization){
        organization->show();
    });
    return 0;
}