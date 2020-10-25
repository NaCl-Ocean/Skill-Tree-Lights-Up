#include <iostream>
using namespace std;
#include "worker.h"

#include <fstream>
#define FILENAME "empfile.txt"
class WorkerManager
{
public:
    
    WorkerManager();
    ~WorkerManager();
    void show_menu();
    void exit_system();
    void add_worker();
    void save();
    void show_workers();
    int get_worker_num();
    void show_worker_info();
    void del_worker();
    void modify_worker();
    void search_worker_wrapper();
    void search_worker(string name);
    void search_worker(int id);
    void sort_worker();
protected:
    int m_empnum;
    Worker ** m_emparray;
    bool FileIsEmpty;

};

