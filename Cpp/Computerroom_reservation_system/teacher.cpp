#include "identity.h"

Teacher::Teacher(){
    order_record = Orderfile();
}
Teacher::Teacher(int id, string name, int password){
    this->id = id;
    this->name = name;
    this->password = password;
    order_record = Orderfile();

}
void Teacher:: show_menu(){
    cout << endl << "欢迎登录: " << this->name << endl;
    cout << "\t\t -----------------------------\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       1.查看所有预约        |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       2.审核预约            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       0.注销登录            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t ------------------------------\n";
    cout << "请输入您的操作:" << endl;
}
void Teacher::show_order(){
    map<string,string> temp;
    for (int i=1;i<=order_record.size;i++){
        temp = order_record.record[i];
        cout << "预约编号:" << i << " 预约时间段:" << order_record.date_map[temp["date"]] 
            << order_record.date_map_2[temp["interval"]] << " 学生学号:" << temp["stuid"]
            << " 学生姓名:" << temp["stuname"] << " 机房编号:" << temp["roomid"] << " 状态:" << order_record.status_map[temp["status"]] << endl;
    }

}
void Teacher::valid_order(){
    int id;
    cout << "请输入要审核的预约编号:" << endl;
    cin >>id;
    order_record.record[id]["status"] = to_string(2);
    cout << "预约通过！" << endl;
    order_record.update();

}


void Teacher::manage(){
    int select;
    while(1){
        this->show_menu();
        cin >> select;
        switch (select)
        {
        case 1:
            show_order();
            break;
        case 2:
            valid_order();
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

void Teacher::show_info(){
    cout << "教师 " << "姓名 "<< this->name<<" 职工号 " << this->id << " 密码 "<< this->password << endl;
}