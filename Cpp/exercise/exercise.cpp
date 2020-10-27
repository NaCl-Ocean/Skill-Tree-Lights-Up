#include <iostream>
using namespace std;
#include <string>
#include "myarray.hpp"
#include <vector>
#include <algorithm>
#include <deque>

class Person{
public:
    int age;
    string name;
    Person(string name,int age){
        this->age = age;
        this->name = name;
    }
};

void print(vector<int> &p){
    for(vector<int>::iterator it = p.begin();it!=p.end();it++){
        cout << *it << " ";
    }

    for (int i=0;i<10;i++){

    }
    cout << endl;
}

int main(){
    deque<int> d1;
    
    return 0;
}