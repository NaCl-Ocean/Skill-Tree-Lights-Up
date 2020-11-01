#include <iostream>
using namespace std;
#include "globalfile.h"
#include <map>
#include <string>
#include <vector>

class Orderfile{
public:
    int size;
    map<int,map<string,string>> record;
    map<string,string> date_map;
    map<string,string> date_map_2;
    map<string,string> status_map;
    Orderfile();
    void update();
    void sort();
};