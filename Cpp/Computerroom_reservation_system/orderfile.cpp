#include "oderfile.h"
#include <fstream>
Orderfile::Orderfile(){
    ifstream ifs;
    ifs.open(ORDER_FILE, ios::in);
    string date,interval,stuname,stuid,roomid,status;
    int id = 0;
    while(ifs >> date && ifs>> interval && ifs>>stuid && ifs>>stuname 
        && ifs>>roomid && ifs>>status){
            id ++;
            string key,value;
            key = date.substr(0, date.find(":"));
            value = date.substr(date.find(":")+1, date.size()-date.find(":")-1);
            this->record[id].insert(make_pair(key,value));
            key = interval.substr(0, interval.find(":"));
            value = interval.substr(interval.find(":")+1, interval.size()-interval.find(":")-1);
            this->record[id].insert(make_pair(key,value));
            key = stuid.substr(0, stuid.find(":"));
            value = stuid.substr(stuid.find(":")+1, stuid.size()-stuid.find(":")-1);
            this->record[id].insert(make_pair(key,value));
            key = stuname.substr(0, stuname.find(":"));
            value = stuname.substr(stuname.find(":")+1, stuname.size()-stuname.find(":")-1);
            this->record[id].insert(make_pair(key,value));
            key = roomid.substr(0, roomid.find(":"));
            value = roomid.substr(roomid.find(":")+1, roomid.size()-roomid.find(":")-1);
            this->record[id].insert(make_pair(key,value));
            key = status.substr(0, status.find(":"));
            value = status.substr(status.find(":")+1, status.size()-status.find(":")-1);
            this->record[id].insert(make_pair(key,value));
        }
    size = id;
    date_map.insert(make_pair("1","周一"));
    date_map.insert(make_pair("2","周二"));
    date_map.insert(make_pair("3","周三"));
    date_map.insert(make_pair("4","周四"));
    date_map.insert(make_pair("5","周五"));
    date_map_2.insert(make_pair("1","上午"));
    date_map_2.insert(make_pair("2","下午"));
    status_map.insert(make_pair("1","尚未审核"));
    status_map.insert(make_pair("2","预约成功"));
    status_map.insert(make_pair("3","取消预约"));

}

void Orderfile::update(){

    ofstream ofs;
    ofs.open(ORDER_FILE,ios::trunc);
    if (this->size==0){
        return;
    }
    for (int i=1;i<=this->size;i++){
        ofs << "date:" << record[i]["date"] << " ";
        ofs << "interval:" << record[i]["interval"] << " ";
        ofs << "stuid:"<< record[i]["stuid"] << " ";
        ofs << "stuname:" << record[i]["stuname"] << " ";
        ofs << "roomid:" << record[i]["roomid"] <<  " "; 
        ofs << "status:" << record[i]["status"] << " ";
        ofs << endl;
    }
    ofs.close();
}