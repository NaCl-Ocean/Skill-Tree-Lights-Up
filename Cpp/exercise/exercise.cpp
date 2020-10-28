#include <iostream>
#include <string>
#include <map>
#include <set>
using namespace std;
 


class MyCompare
{
 
public:
    bool operator()(string s1, string s2)
    {
        return s1 > s2;
    }
 
};


int main()
{
    
    map<string, int, MyCompare> m;
 
    // map容器默认排序
    m.insert(make_pair("Tom", 18));
    m.insert(make_pair("Anthony", 23));
    m.insert(make_pair("Bob", 24));
    m.insert(make_pair("Sunny", 19))；
    
    return 0;
}
