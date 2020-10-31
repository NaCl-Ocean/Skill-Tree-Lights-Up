#include <iostream>
using namespace std;
#include "manager.h"
#include <algorithm>
#include <map>


int main(){
    //for_each(manger.speakers.begin(), manger.speakers.end(), print);
    while(1){
        Manager manger;
        int choice; 
        Print_speaker print = Print_speaker(& manger.speakers);
        manger.show_menu();
        cin >> choice;
        switch (choice)
        {
        case 0:
            manger.start_competition();
            manger.competition();
            //for_each(manger.v1.begin(),manger.v1.end(),print);
            break;
        case 1:
            manger.load();
            break;
        case 2:
            manger.reset();
            break;
        case 3:
            manger.exit_system();
            break;
        default:
            cout << "输入错误，请重新输入" << endl;
            break;
        }
    }
}
