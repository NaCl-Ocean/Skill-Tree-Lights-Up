#include <iostream>
using namespace std;
#include "globalfile.h"
#include "identity.h"
#include <fstream>



void show_login(){
    cout << "=====================  欢迎来到机房预约系统  =====================" << endl;
    cout << endl << "请输入您的身份:" << endl;
    cout << "\t\t -----------------------------\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       1.学生代表            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       2.老   师             |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       3.管 理 员            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       0.退   出             |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t ------------------------------\n";
    cout << "请输入您的选择:" << endl;
}

void login(string file_name, int type){
    Identity * user;

    ifstream ifs;
    ifs.open(file_name, ios::in);

    if (!ifs.is_open()){
        cout << "文件不存在"<< endl;
        system("reset");
        ifs.close();
        return;
    }

    string name;
    int id;
    int passwd;

    cout << "请输入您的姓名:"<< endl;
    cin>>name;
    if (type==1){
        cout << "请输入您的学号:"<< endl;
        cin >>id;
    }else if(type==2){
        cout << "请输入您的职工号:"<< endl;
        cin >> id;
    }
    cout << "请输入密码:"<< endl;
    cin >> passwd;
    if (type==1){
        int f_id,f_password;
        string f_name;
        while(ifs>>f_id && ifs>>f_name && ifs>>f_password){
            if (f_id==id && f_name==name && f_password==passwd){
                cout << "登录成功!"<<endl;
                user = new Student(id,name,passwd);
                Student * stu = (Student *)user;
                stu->manage();
                delete stu;
                return;
            }
        }

    }else if(type==2){
        int f_id,f_password;
        string f_name;
        while(ifs>>f_id && ifs>>f_name && ifs>>f_password){
            if (f_id==id && f_name==name && f_password==passwd){
                cout << "登录成功!"<<endl;
                user = new Teacher(id,name,passwd);

                Teacher *tea = (Teacher *)user;
                tea->manage();
                delete tea;
                return;
            }
        }

    }else if(type==3){
        int f_password;
        string f_name;
        while(ifs>>f_name && ifs>>f_password){
            if (f_name==name && f_password==passwd){
                cout << "登录成功!"<<endl;
                user = new Admin(name,passwd);
                Admin *admin = (Admin *)user;
                admin->manage();
                delete admin;
                return;
            }
        }

    }else{

    };
    cout << "验证登录失败...."<< endl;
    cout << "请重新输入您的选择:" << endl;
    return;
}





int main(){
    int select;
    string temp;
    while(1){
        show_login();
        cin >> select;
        switch (select)
        {
        case 1://学生
            login(STUDENT_FILE,1);
            break;
        case 2://教师
            login(TEACHER_FILE,2);
            break;
        case 3://管理员
            login(ADMIN_FILE,3);
            break;
        case 0:
            cout << "欢迎下次使用"<<endl;
            cin.get();
            return 0;
            break;
        default:
            cout << "输入错误，请重新输入"<<endl;
            cin.get();
            break;
        }

    }
    return 0;
}