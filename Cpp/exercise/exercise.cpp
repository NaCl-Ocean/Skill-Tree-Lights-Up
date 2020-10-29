#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <stack>
using namespace std;
#include <algorithm>
#include <functional>
#include <numeric>

class Person{
public:
    string name;
    int sex;
    int age;
    Person(string name, int sex, int age){
        this -> name = name;
        this -> sex = sex;
        this -> age = age;
    }
    Person(const Person &p){
        this->name = p.name;
        this->sex = p.sex;
        this->age = p.age;
    }
public:
    bool operator<(const Person &person) const{
        if (age<person.age){
            return true;
        }else{
            return false;
        }
    }
};

class Myreplace{
public:
    bool operator()(const Person &p1)const{
        if (p1.name == "tom"){
            return true;
        }else{
            return false;
        }
    }
};
bool Mycompare2(const Person &p1, const Person p2){
    if (p1.age < p2.age){
            return false;
        }else{
            return false;
        }
}
void print(int v){
    cout<< v << " ";
}
int main()
{   
    vector<int> v1;
    vector<int> v2;
    for(int i=0;i<10;i++){
        v1.push_back(i+1);
        v2.push_back(i+5);
    }
    vector<int> v3;
    v3.resize(10);
    vector<int>::iterator end1 = set_intersection(v1.begin(),v1.end(),v2.begin(),v2.end(),v3.begin());
    for_each(v3.begin(),end1,print);
    cout<<endl;

    vector<int> v4;
    v4.resize(20);
    vector<int>::iterator end2 = set_union(v1.begin(),v1.end(),v2.begin(),v2.end(),v4.begin());
    for_each(v4.begin(),end2,print);
    cout<<endl;
    vector<int> v5;
    v5.resize(10);
    vector<int>::iterator end3 = set_difference(v1.begin(),v1.end(),v2.begin(),v2.end(),v5.begin());
    for_each(v5.begin(),end3,print);
    cout<<endl;

    return 0;
}
