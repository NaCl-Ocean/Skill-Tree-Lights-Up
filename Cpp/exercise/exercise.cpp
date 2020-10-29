#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
using namespace std;
#include <algorithm>
#include <functional>

class GreatFive{
public:
    bool operator()(int v){
        return v>5;
    }
};

class descend{
public:
    bool operator()(int v1,int v2){
        return v1>v2;
    }

};
int main()
{
    vector<int> v;
    for (int i=0;i<7;i++){
        v.push_back(rand()%100);
    }
  	// 默认排序(升序)
    sort(v.begin(),v.end());
    for (vector<int> ::iterator it=v.begin();it!=v.end();it++){
        cout << *it << " ";
    }
    cout << endl;
 		// 降序
    sort(v.begin(),v.end(),greater<int>());
    for (vector<int> ::iterator it=v.begin();it!=v.end();it++){
        cout << *it << " ";
    }
    cout << endl;
    return 0;
}
