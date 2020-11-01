#include <iostream>
using namespace std;
#include <vector>
#include "computeroom.h"
#include "oderfile.h"
class Identity{
public:
    string name;
    int password;
    virtual void show_menu()=0;

};

class Student: public Identity{
public:
    int id;
    vector<ComputerRoom> computer_rooms;
    Orderfile order_record;
    Student();
    Student(int id, string name, int password);
    void show_menu();
    void apply_order();
    void show_my_order();
    void show_all_order();
    void cancel_order();
    void manage();
    void show_info();
    void init_computer_room();
    void show_computerroom_info();
};

class Teacher:public Identity{
public:
    int id;
    Orderfile order_record;
    Teacher();
    Teacher(int id, string name, int password);
    void show_menu();
    void show_order();
    void valid_order();
    void manage();
    void show_info();
};

class Admin:public Identity{
public:
    Admin();
    Admin(string name,int password);
    vector<ComputerRoom> computer_rooms;
    void show_menu(); 
    void add_user();  
    void show_user_info();
    void show_computerroom_info();
    void clean_file();
    void manage();
    vector<Student> v_stu;
    vector<Teacher> v_tea;
    void init_vector();
    bool is_repeat(int id, int type);
    void init_computer_room();
    void modify_computer_room();
    void save_computer_room();
};