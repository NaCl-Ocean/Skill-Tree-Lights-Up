#include "identity.h"
#include "globalfile.h"
#include <fstream>
#include <algorithm>
Admin::Admin(){
    this->init_vector();
    this->init_computer_room();
}
Admin::Admin(string name,int password){
    this->name = name;
    this->password = password;
    this->init_vector();
    this->init_computer_room();

}
void Admin::show_menu(){
    cout << endl << "欢迎登录: " << this->name << endl;
    cout << "\t\t -----------------------------\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       1.添加账号            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       2.查看账号            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       3.查看机房            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       4.清空预约            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       5.修改机房信息        |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       0.注销登录            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t ------------------------------\n";
    cout << "请输入您的操作:" << endl;

}
void Admin::add_user(){
    cout << "请输入要添加的账号类型: 1.学生 2.教师" << endl;
    int type;
    bool correct=false;
    string file;
    while (correct==false){
        cin >> type;
        switch (type)
        {
            case 1:
                correct = true;
                file = STUDENT_FILE;
                break;
            case 2:
                correct = true;
                file = TEACHER_FILE;
                break;
            default:
                cout << "输入错误，请重新输入:"<< endl;
                correct= false;
                break;
        }
    }
    string name;
    int password,id,password_2;
    cout << "请输入姓名:"<< endl;
    cin >> name;
    correct = false;
    while(correct==false){
        cout << "请输入学号/职工号:"<< endl;
        cin >> id;
        correct = this->is_repeat(id,type);
        correct = !correct;
        if (correct==false){
            cout << "学号/职工号重复" << endl;
        }
    }
    cout <<"请输入密码:"<<endl;
    cin>> password;
    ofstream ofs;
    ofs.open(file,ios::app|ios::out);
    ofs << id<< " " << name << " " << password << endl;
    ofs.close();

    if (type==1){
        this->v_stu.push_back(Student(id,name,password));
    }else if(type==2){
        this->v_tea.push_back(Teacher(id,name,password));
    }else{

    }
    cout << "添加成功"<< endl;
}
void Admin::show_user_info(){
    cout << "请选择查看内容:1.学生 2.老师" << endl;
    int select;
    cin >> select;
    if (select==1){
        for(vector<Student>::iterator it=v_stu.begin();it!=v_stu.end();it++){
            (*it).show_info();
        }
    }else if(select==2){
        for(vector<Teacher>::iterator it=v_tea.begin();it!=v_tea.end();it++){
            (*it).show_info();
        }
    }else{
        cout << "输入错误,返回上一级菜单"<< endl; 
    }

}
void Admin::show_computerroom_info(){
    cout << "机房信息如下：" << endl;
    for(vector<ComputerRoom>::iterator it=computer_rooms.begin();it!=computer_rooms.end();it++){
        (*it).show_info();
    }
}
void Admin::clean_file(){
    ofstream ofs;
    string choice;
    cout << "确定要清空？Y/n" << endl;
    cin >> choice;
    if (choice=="Y"){
        cout << "清空成功！" << endl;
        ofs.open(ORDER_FILE,ios::trunc);
    }else{
        return;
    }
}


void Admin::init_vector(){
    this->v_tea.clear();
    this->v_stu.clear();
    ifstream ifs;
    ifs.open(STUDENT_FILE, ios::in);
    if (!ifs.is_open()){
        cout << "文件不存在"<< endl;
        system("reset");
        ifs.close();
        return;
    }

    int id,password;
    string name;
    while(ifs>>id && ifs>>name && ifs>>password){
        this->v_stu.push_back(Student(id,name,password));
    }
    cout << "当前学生数量:"<< this->v_stu.size() << endl;
    ifs.close();
    ifs.open(TEACHER_FILE,ios::in);
    if (!ifs.is_open()){
        cout << "文件不存在"<< endl;
        system("reset");
        ifs.close();
        return;
    }
    while(ifs>>id && ifs>>name && ifs>>password){
        this->v_tea.push_back(Teacher(id,name,password));
    }
    cout << "当前教师数量:"<< this->v_tea.size() << endl;
}



void Admin::manage(){
    while(1){
        this->show_menu();
        int select;
        cin >> select;
        switch (select)
        {
        case 1:
            this->add_user();
            cin.get();
            break;
        case 2:
            this->show_user_info();
            cin.get();
            break;
        case 3:
            this->show_computerroom_info();
            cin.get();
            break;
        case 4:
            this->clean_file();
            cin.get();
            break;
        case 5:
            this->modify_computer_room();
            cin.get();
            break;
        case 0:
            system("reset");
            return;
            break;
        default:
            cout << "输入错误，请重新输入"<<endl;
            break;
        }
    }
}

bool Admin::is_repeat(int id, int type){
    if(type==1){
        for(vector<Student>::iterator it=v_stu.begin();it!=v_stu.end();it++){
            if((*it).id==id){
                return true;
            }
        }
    }else if(type==2){
        for(vector<Teacher>::iterator it=v_tea.begin();it!=v_tea.end();it++){
            if((*it).id==id){
                return true;
            }
        }
    }else{
        return false;
    }
    return false;
}

void Admin::init_computer_room(){
    ifstream ifs;
    int capacity,id,size;
    ifs.open(COMPUTER_FILE,ios::in);
    if(!ifs.is_open()){
        cout << "文件不存在"<< endl;
        ifs.close();
        return;
    }
    while(ifs>>id && ifs>>size && ifs>>capacity){
        this->computer_rooms.push_back(ComputerRoom(id,size,capacity));
    }
}


void Admin::modify_computer_room(){
    cout << "请输入要修改的类型: 1.增加机房  2.修改现有机房的最大容量"<< endl;
    int choice;
    int capacity;
    cin >> choice;

    switch (choice)
    {
    case 1:
        cout << "请输入要增加机房的最大容量:"<< endl;
        cin >> capacity;
        computer_rooms.push_back(ComputerRoom(computer_rooms.size()+1,capacity,capacity));
        break;
    case 2:
        cout << "请输入要修改机房的编号:"<< endl;
        int id;
        cin >> id;
        cout << "请输入容量:" << endl;
        cin >> capacity;
        int old_capacity;
        old_capacity = computer_rooms[id-1].capacity;
        computer_rooms[id-1].capacity = capacity;
        computer_rooms[id-1].size += capacity - old_capacity;
        break;
    default:
        cout << "输入错误，返回上一级菜单"<< endl;
        return;
        break;
    }
    this->save_computer_room();
}

void Admin::save_computer_room(){
    ofstream ofs;
    ofs.open(COMPUTER_FILE,ios::out);
    for(vector<ComputerRoom>::iterator it=computer_rooms.begin();it!=computer_rooms.end();it++){
        ofs << (*it).id << " " << (*it).size << " " << (*it).capacity << endl;
    }
}