#include <iostream>
using namespace std;
#include <string>


class Base{
public:
    int age;
    Base(int age){
        this->age = age;
        cout << "father parameter cnostruction function" << endl;

    }
    void operator<<(Base &p){
        cout << p.age<<endl;
    }
    
};

class Son1:public Base{
public:
    Son1(int age):Base(age){
        cout << "son parameter construction function" << endl;
    }
};

class Son2:public Base{
public:
    Son2():Base(5){
        cout << "son no parameter construction function" << endl;
    }
};

int main(){
    Base b = Base(5);
    Base c = Base(6);
    b<<c;
    Son1 s1 = Son1(5);
    Son2 s2 = Son2();
    return 0;
}
