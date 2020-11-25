#include "swap.h"

void Swap(int &a, int &b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}