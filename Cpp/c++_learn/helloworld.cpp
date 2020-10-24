#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Base{
public:
    virtual ~ Base(){
        cout << "virtual father func" << endl;
    }
};

class Son: public Base{
public:
    ~Son(){
        cout << "virtual son function" << endl;
    }
};

class Base2{
public:
    ~Base2(){
        cout << "father func" << endl;
    }
};
class Son2:public Base2{
public:
    ~Son2(){
        cout << "son function" << endl;
    }
};


int main(){
    int a[5] = {1,2,3,4,5};
    int *p = a;
    cout << *p << endl;


    return 0;
}