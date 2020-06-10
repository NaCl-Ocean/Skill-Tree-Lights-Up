#include <iostream>
using namespace std;
#include <string>

class Cube
{
private:
    int l;
    int w;
    int h;
    int area;
    int v;
public:
    void cal_v(){
        v = l*w*h;
    }
    int get_v(){
        return v;
    }
    void set_l(int l_input){
        l = l_input;
    }
    void set_h(int h_input){
        h = h_input;
    }
    void set_w(int w_input){
        w = w_input;
    }
    int get_h(){
        return h;
    }
    void cal_a(){
        area = l*w;
    }
public:
    Cube(const Cube &c){
        cout<<"using reference construct"<<endl;
    }
    Cube(){
        cout<<"using basic construct"<<endl;
    }
};


bool issame(Cube cube_1, Cube cube_2)
{
    cout<<cube_2.get_h()<<endl;
    cube_2.set_h(20);
    cout<<cube_2.get_h()<<endl;
    return (cube_1.get_v() == cube_2.get_v());
}
int main(){
    Cube cube_1;
    cube_1.set_h(10);
    cube_1.set_w(20);
    cube_1.set_l(30);
    cube_1.cal_v();
    Cube cube_2;
    cube_2.set_h(10);
    cube_2.set_w(20);
    cube_2.set_l(30);
    cube_2.cal_v();
    bool res;
    res = issame(cube_1,cube_2);
    cout<<cube_2.get_h()<<endl;
    cout << res <<endl;
}