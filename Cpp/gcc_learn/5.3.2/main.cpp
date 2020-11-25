#include <iostream>
using namespace std;
#include "swap.h"

int main(){
    int a = 10;
    int b = 20;
    cout << "befor swap, a:" << a << " b:"<<b << endl;
    swap(a,b);
    cout << "after swap, a:" << a << " b:"<<b << endl;
}