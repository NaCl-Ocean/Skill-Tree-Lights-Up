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
    Person(){
        this->name = "test";
        this->sex = 10;
        this->age = 5;
    }
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
    string get_name(){
        return name;
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

int main()
{   
    map<int,Person> m1;
    m1.insert(make_pair(12,Person("tom",10,23)));
    m1.insert(make_pair(13,Person("jack",10,23)));
    map<int,Person> *m2 = &m1;
    cout << (*m2)[12].get_name() << endl;
    vector<int> v1;
    v1.push_back(10);
    srand(10);
    
    // //v2.resize(3,Person("tom",2,23));
    // //replace_if(v1.begin(),v1.end(),Myreplace(),Person("jack",1,18));
    // copy(m1.begin(),m1.end(),m2.begin());
    // for (vector<Person>::iterator it=v2.begin(); it!= v2.end(); it++){
    //     cout << "姓名：" << it->name << " 年龄:" << it->age << "性别:" << it->sex << endl;
    // }
    return 0;
}