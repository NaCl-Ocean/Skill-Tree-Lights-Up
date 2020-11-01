#include <iostream>
using namespace std;


class ComputerRoom{
public:
    int capacity;
    int id;  
    int size;
    ComputerRoom(int id,int size,int capacity){
        this->capacity =capacity;
        this->size = size;
        this->id = id;
    }
    void show_info(){
        cout << "机房编号: "<< this->id<<" 机房容量: " << this->size <<" 机房最大容量: " << this->capacity << endl;
    }
};