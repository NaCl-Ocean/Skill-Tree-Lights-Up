#include <iostream>
using namespace std;
#include "workerManager.h"





int main()
{
    
    WorkerManager wm;
    int choice = 0;
    while(1){
        wm.show_menu();
        cout << "********* 请输入你的选择 *********" << endl;
        cin >> choice;
        switch (choice)
        {
        case 0:
            wm.exit_system();
            break;
        case 1:
            wm.add_worker();
            wm.save();
            break;
        case 2:
            wm.show_worker_info();
            break;
        case 3:
            wm.del_worker();
            break;
        case 4:
            wm.modify_worker();
            break;
        case 5:
            wm.search_worker();
            break;
        case 6:
            
            break;
        case 7:
            break;
        default:
            cout << "输入错误，请重新输入" << endl;
            break;
        }
    }
    return 0;
}