#include <iostream>
using namespace std;


template <typename T>
class MyArray{
public:

    MyArray(int capacity){
        this->capacity = capacity;
        this->size = 0;
        this->address = new T[this->capacity];
    }

    MyArray(const MyArray<int> &arr){
        this->capacity = arr.capacity;
        this->size = arr.size;
        this->address = new T[this->capacity];
        for (int i=0;i<this->capacity;i++){
            this->address[i] = arr.address[i];
        }
    }
    ~MyArray(){
        if (this->address != NULL){
            this->capacity = 0;
            this->size = 0;
            delete[] this->address;
            this->address = NULL;
        }
    }

    MyArray & operator=(const MyArray & arr){
        if(this->address !=NULL){
            delete[] this->address;
        }
        this->capacity = arr.capacity;
        this->size = arr.size;
        this->address = new T[this->capacity];
        for (int i=0;i<this->capacity;i++){
            this->address[i] = arr.address[i];
        }
        return *this;
    }

    void show(){
        if (this->address != NULL & size >0){
            for (int i=0;i < this->size; i++){
                cout << this->address[i]<< " ";
            }
            cout << endl;
        }
    }

    void push(const T & value){
        if (size == capacity){
            cout << "无法再插入元素"<< endl;
            return;
        }
        address[size] = value;
        size ++;
    }

    void pop(){
        if (size == 0){
            return;
        }
        size -- ;
    }

    T& operator[](int index){
        return address[index];
    }

    int get_capacity(){
        return capacity;
    }

    int get_size(){
        return size;
    }

private:
    int capacity;
    int size;
    T *address;
};
