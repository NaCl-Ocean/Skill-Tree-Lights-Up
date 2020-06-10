#include <iostream>
using namespace std;


int swap(const int* a, const int* b){
    cout<<"using const"<<endl;
    return (*a +*b);
}
int swap(int *a,int *b){
    cout<<"using no const"<<endl;
    return (*a+*b);
}
int main(){
    int a =10;
    int b=20;
    swap(&a,&b);
    const int & c = 10;
}