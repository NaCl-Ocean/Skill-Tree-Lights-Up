#include <iostream>
using namespace std;
#include <string>
#include <vector>
#include <map>
#include "speaker.h"
class Manager{
public:
    vector<int> v1;
    vector<int> v2;
    vector<int> v3;
    map<int,vector<string> > record;
    map<int,Speaker> speakers;
    bool file_not_exist = false;
    bool file_empty = false;
    int index;
    Manager();
    ~Manager();
    void show_menu();
    void exit_system();
    void create_speaker();
    void start_competition();
    void competition();
    void show_promoted();
    void draw();
    void save();
    void load();
    void show_record();
    void reset();
};


class Print_speaker{
public:
    map<int,Speaker> *speakers;
    void operator()(int index);
    void operator()(const pair<int,Speaker> &p);
    Print_speaker(map<int,Speaker> * const speakers);
};