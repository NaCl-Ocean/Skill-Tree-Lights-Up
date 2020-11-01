#include "identity.h"
#include <fstream>
#include "globalfile.h"


Student::Student(){
    this->init_computer_room();
    this->order_record = Orderfile();
}

Student::Student(int id, string name, int password){
    this->name = name;
    this->id = id;
    this->password = password;
    this->init_computer_room();
    this->order_record = Orderfile();
}

void Student::show_menu(){
    cout << endl << "欢迎登录: " << this->name << endl;
    cout << "\t\t -----------------------------\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       1.申请预约            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       2.查看我的预约        |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       3.查看所有预约        |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       4.取消预约            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t|       0.注销登录            |\n";
    cout << "\t\t|                             |\n";
    cout << "\t\t ------------------------------\n";
    cout << "请输入您的操作:" << endl;
}
void Student::apply_order(){
    this->show_computerroom_info();
    int date,room,interval;
    cout << "请输入要预约的时间:1.周一 2.周二 3.周三 4.周四 5.周五"<< endl;
    cin >> date;
    bool correct=false;
    while (correct==false){
        cout << "请输入要预约的机房"<< endl;
        cin >> room;
        if(this->computer_rooms[room-1].size == 0){
            cout << "该机房已满，请选择其他机房预约"<< endl;
            correct = false;
        }else{
            correct = true;
        }
    }
    cout << "请输入要预约的时间段:1.上午 2.下午" << endl;
    cin >> interval;

    order_record.record[order_record.size+1].insert(make_pair("date", to_string(date)));
    order_record.record[order_record.size+1].insert(make_pair("interval", to_string(interval)));
    order_record.record[order_record.size+1].insert(make_pair("stuid", to_string(this->id)));
    order_record.record[order_record.size+1].insert(make_pair("stuname", this->name));
    order_record.record[order_record.size+1].insert(make_pair("roomid", to_string(room)));
    order_record.record[order_record.size+1].insert(make_pair("status", to_string(1)));
    order_record.size++;
    order_record.update();
}
void Student::show_my_order(){
    map<string,string> temp;
    for(int i=1;i< order_record.size;i++){
        if(order_record.record[i]["stuid"]==to_string(this->id)){
            temp = order_record.record[i];
            cout << "预约编号:" << i << " 预约时间段:" << order_record.date_map[temp["date"]] 
            << order_record.date_map_2[temp["interval"]] << " 机房编号:" << temp["roomid"] 
            << " 状态:" << order_record.status_map[temp["status"]] << endl;
        }
    }
}
void Student::show_all_order(){
    map<string,string> temp;
    for (int i=1;i<=order_record.size;i++){
        temp = order_record.record[i];
        cout << "预约编号:" << i << " 预约时间段:" << order_record.date_map[temp["date"]] 
            << order_record.date_map_2[temp["interval"]] << " 学生学号:" << temp["stuid"]
            << " 学生姓名:" << temp["stuname"] << " 机房编号:" << temp["roomid"] << " 状态:" << order_record.status_map[temp["status"]] << endl;
    }

}
void Student::cancel_order(){
    int id;
    cout << "请输入要取消的预约编号:" << endl;
    cin >> id;
    order_record.record[id]["status"] = to_string(3);
    cout << "取消成功！" << endl;
    order_record.update();

}


void Student::manage(){
    int select;
    while(1){
        this->show_menu();
        cin >> select;
        switch (select)
        {
        case 1:
            apply_order();
            break;
        case 2:
            show_my_order();
            break;
        case 3:
            show_all_order();
            break;
        case 4:
            cancel_order();
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

void Student::show_info(){
    cout << "学生 " << "姓名 "<< this->name<<" 学号 " << this->id << " 密码 "<< this->password << endl;
}

void Student::init_computer_room(){
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

void Student::show_computerroom_info(){
    cout << "当前机房信息如下：" << endl;
    for(vector<ComputerRoom>::iterator it=computer_rooms.begin();it!=computer_rooms.end();it++){
        (*it).show_info();
    }
}