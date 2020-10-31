#include <iostream>
using namespace std;
#include "manager.h"
#include <random>
#include <algorithm>
#include <deque>
#include <fstream>

void Print_speaker::operator()(const pair<int,Speaker> &p){
    cout << "id:" << p.first << " name:" << p.second.name << 
    " score[0]:" << p.second.score[0] << " score[1]:" << p.second.score[1] << endl;

}
void Print_speaker::operator()(int index){
   cout << "id:" << index << " name:" << (*this->speakers)[index].name << 
    " score[0]:" << (*this->speakers)[index].score[0] << " score[1]:" << (*this->speakers)[index].score[1] << endl;
}

Print_speaker::Print_speaker(map<int,Speaker> * const speakers){
    this->speakers = speakers;
}
void Manager::show_menu(){
    cout << "************************************************" << endl;
    cout << "**************** 欢迎参加演讲比赛！ ********" << endl;
    cout << "**************** 0.开始演讲比赛 ****************" << endl;
    cout << "**************** 1.查看往届记录 ****************" << endl;
    cout << "**************** 2.清空比赛记录 ****************" << endl;
    cout << "**************** 3.退出比赛程序 ****************" << endl;    
    cout << endl;
}


void Manager::exit_system(){
    cout << "欢迎下次使用" << endl;
    cin.get();
    exit(0);
}

void Manager::create_speaker(){
    string nameseed="ABCDEFGHIJKLMNOPQRST";
    for (int i=0;i<12;i++){
        string name = "选手";
        name += nameseed[i];
        Speaker sp = Speaker(name);
        this->speakers.insert(make_pair(i+1001, sp));
        this->v1.push_back(i+1001);
    }
}

Manager::Manager(){
    // init
    this->v1.clear();
    this->v2.clear();
    this->v3.clear();
    this->index = 0;
    this->speakers.clear();
    // create speaker
    this->create_speaker();

}


Manager::~Manager(){}

void Manager::draw(){
    cout << "第" << this->index << "轮比赛，开始抽签" << endl;
    std::random_device rd;
    std::mt19937 g(rd());
    if (index==1){
        std::shuffle(this->v1.begin(),this->v1.end(),g);

    }else if(index==2){
        std::shuffle(this->v2.begin(),this->v2.end(),g);
    }else{
        
    }
}

void Manager::start_competition(){
    this->index = 1;
    this->draw();
}
void Manager::competition(){
    while (this->index!=3){
        int num = 1;
        cout << "第" << this->index << "轮比赛，开始比赛" << endl;
        vector<int> v;
        multimap<double,int,greater<double>> group_score;
        if (this->index == 1){
            v = v1;
        }else{
            v = v2;
        }
        for(vector<int>::iterator it=v.begin();it!=v.end();it++){
            deque<double> scores;
            for (int i=0;i<10;i++){
                double score= (rand()%401 + 600)/10; 
                scores.push_back(score);
            }
            sort(scores.begin(),scores.end());
            // 去头去尾
            scores.pop_back();
            scores.pop_front();
            double sum = accumulate(scores.begin(),scores.end(),0);
            double avg = sum/(scores.size());
            this->speakers[*it].score[this->index-1] = avg;
            
            group_score.insert(make_pair(avg,*it));
            if (num%6==0){
                cout << "第" << num/6 << "小组比赛名次" << endl;
                for (multimap<double,int,greater<double>>::iterator it=group_score.begin();it!=group_score.end();it++){
                    cout << "编号:" << (*it).second << "姓名:" << this->speakers[(*it).second].name
                        <<"score:"<< this->speakers[(*it).second].score[this->index-1]<<endl;
                }
                // 晋级
                int num_ = 1;
                for(multimap<double,int,greater<double>>::iterator it=group_score.begin();it!=group_score.end();it++){
                    if (num_<=3){
                        if(this->index == 1){
                            v2.push_back((*it).second);
                        }else{
                            v3.push_back((*it).second);
                        }
                    }
                    num_ ++ ;
                }

                group_score.clear();
            }
            num ++;
        }

        cout << "本轮比赛结束"<< endl;
        this->index ++;
        this->show_promoted();
        cin.get();
    }

    this->save();
    cout <<"本届比赛完毕"<< endl;
    cin.get();
    
}
void Manager::show_promoted(){
    cout << "---------------第" << (this->index-1 )<< "轮晋级信息如下---------------" << endl;
    vector<int> v;
    if (this->index == 2){
        v = v2;
    }else if (this->index == 3){
        v = v3;
    }
    for(vector<int>::iterator it=v.begin();it!=v.end();it++){
        cout << "编号:" << *it << " 姓名:" << this->speakers[*it].name
                    <<" score:"<< this->speakers[*it].score[this->index-2]<<endl;
    }
}

void Manager::save(){
    ofstream ofs;
    ofs.open("record.csv",ios::out|ios::app);
    for (vector<int>::iterator it=this->v3.begin();it!=this->v3.end();it++){
        ofs << *it << "," << this->speakers[*it].score[1] << ","; 
    }
    ofs<<endl;
    ofs.close();

}


void Manager::load(){
    ifstream ifs;
    ifs.open("record.csv",ios::in);
    // 文件不存在
    if (!ifs.is_open()){
        cout << "文件不存在" << endl;
        ifs.close();
        file_not_exist = true;
        return;
    }
    // 文件内容为空
    char ch;
    ifs >> ch;
    if (ifs.eof()){
        cout << "文件内容为空" << endl;
        file_empty = true;
        ifs.close();
        return;
    }

    // 文件中有内容
    ifs.putback(ch);
    string data;
    int n=1;
    while(ifs>>data){
        
        int pos;
        int start=0;
        while (true){
            pos = data.find(",", start);
            if (pos==-1){
                break;
            }
            this->record[n].push_back(data.substr(start,pos-start));
            //cout << data.substr(start,pos-start) << endl;
            start = pos+1;
        }
        n++;
    }
    ifs.close();
    this->show_record();
    cin.get();

}

void Manager::show_record(){
    if (file_not_exist){
        cout << "文件不存在" << endl;
        return;
    }
    if (file_empty){
        cout << "文件为空"<< endl;
        return;
    }
    vector<string> s;
    for(map<int,vector<string>>::iterator it=this->record.begin();it!=this->record.end();it++){
        cout << "第" << (*it).first << "届"<<endl;
        s = (*it).second;
        cout << "冠军编号:"<< s[0] << " 分数:"<< s[1] << " 亚军编号:"<< s[2] << " 分数:" << s[3]
        <<" 季军编号:"<< s[4] << " 分数:"<< s[5] << endl;
    }
}

void Manager::reset(){
    char choice;
    cout << "是否要退出？Y/n"<< endl;
    cin >> choice;
    if (choice != 'Y'){
        return;
    }
    ofstream ofs;
    ofs.open("record.csv",ios::trunc);
    this->v1.clear();
    this->v2.clear();
    this->v3.clear();
    this->speakers.clear();
    this->index = 0;
    cout << "清空成功"<< endl;

}

