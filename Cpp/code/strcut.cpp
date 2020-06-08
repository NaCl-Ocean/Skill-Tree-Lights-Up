#include <iostream>

using namespace std;


struct student{
    int age;
    string name;
    int score;
};
int main(){
    const student s1={20,"hh",80};
    s1.age=60;
}