#include <iostream>

using namespace std;
void swap(int **a);
int main(){
    int a[2][2]= {{2,3},{4,5}};
    int *p[2] = {a[0],a[1]} ;
    int (*pa)[2] = a;
    int *pp = *a;
    for (int i=0;i<4;i++){
        cout<<*pp<<endl;
        pp++;
    }
    cout<<pa[1][1]<<endl;
    pa++;
    cout<<pa<<endl;
    cout<<*pa<<endl;
    cout<<**pa<<endl;
    cout<<p<<endl;
    cout<<*p<<endl;
    cout << **p<<endl;
    int **p2;
    p2 = p;
    cout<<p2<<endl;
    cout<<*p2<<endl;
    cout<<**p2<<endl;
    // p2++;
    cout<<**p2<<endl;
    // cout<<*((*a)++)<<endl;
    // for (int j=0;j<2;j++){
    //     p = a[j];
    //     for(int i=0;i<2;i++){
    //         cout<<*p<<" ";
    //         p++;
    //     }
    //     cout<<"\n";
    // }
    int b[2]={0,0};
    swap(p2);
} 


void swap(int **a){
    cout<<a[1]<<endl;
    cout<<a[0]<<endl;
    cout<<*a<<endl;
    cout<<(*a)[1]<<endl;
}