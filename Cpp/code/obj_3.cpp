#include <iostream>
using namespace std;
#include <string>

class man{
public:
    int name;
    /*类内声明*/
    static int sex;

};
/* 类外初始化 */
int man::sex = 1;


int main(){
    int *p = NULL;
    // cout<<*p<<endl;
    man jack = man();
    cout<<sizeof(jack)<<endl;

}