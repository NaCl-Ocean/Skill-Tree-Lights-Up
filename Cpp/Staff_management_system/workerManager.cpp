#include "workerManager.h"



void WorkerManager::show_menu(){
    cout << "************************************************" << endl;
    cout << "**************** 欢迎使用职工管理系统！ ********" << endl;
    cout << "**************** 0.退出管理程序 ****************" << endl;
    cout << "**************** 1.增加职工信息 ****************" << endl;
    cout << "**************** 2.显示职工信息 ****************" << endl;
    cout << "**************** 3.删除离职员工 ****************" << endl;    
    cout << "**************** 4.修改职工信息 ****************" << endl;
    cout << "**************** 5.查找职工信息 ****************" << endl;
    cout << "**************** 6.按编号排序职工 ****************" << endl;
    cout << "**************** 7.清空所有文档 ****************" << endl;
    cout << endl;
}

void WorkerManager::exit_system(){
    cout << "欢迎下次使用" << endl;
    cin.get();
    exit(0);
}

void WorkerManager::add_worker(){
    cout << "请输入需要添加的员工数量" << endl;
    int add_num;
    cin >> add_num;
    if (add_num == 0){
        cout << "输入错误，请重新输入" << endl;
        return ;
    }

    
    int newsize = this->m_empnum + add_num;
    Worker ** newspace = new Worker *[this->m_empnum];
    if (this->m_emparray != NULL){
        for(int i=0; i<this->m_empnum; i++){
            newspace[i] = this->m_emparray[i];
        }
    }

    for (int i=0;i<add_num;i++){
        int id;
        string name;
        int select;
        cout << "请输入要添加的员工姓名" << endl;
        cin >> name;
        cout << "请输入要添加的员工编号" << endl;
        cin >> id;
        cout <<  "请输入要添加的员工岗位" << endl;
        cout << "1. 老板" << endl;
        cout << "2. 经理" << endl;
        cout << "3. 普通员工" << endl;
        cin >> select;
        Worker * worker = NULL;

        switch (select)
        {
        case 1:
            worker = new Boss(id, name);
            break;
        case 2:
            worker = new Manager(id, name);
            break;
        case 3:
            worker = new Employer(id, name);
            break;
        default:
            cout << "输入错误，请重新输入" << endl;
            break;
        }
        this->FileIsEmpty =  false;
        newspace[this->m_empnum+i] = worker;
    }

    delete[] this->m_emparray;
    this->m_emparray = newspace;
    this->m_empnum = newsize;

    cout << "成功添加" << add_num << "名新职工" << endl;
    cout << "现共有" << this->m_empnum << "名职工" << endl;


}

int WorkerManager::get_worker_num(){
    int num = 0;
    ifstream ifs;
    ifs.open(FILENAME, ios::in);
    int id, did;
    string name;
    getline(ifs, name);
    while (ifs >> id && ifs >> name && ifs >>did){
        num ++;
    }
    return num;
}
void WorkerManager::save(){
    ofstream ofs;
    ofs.open(FILENAME, ios::out);
    ofs<<"record:";
    if(this->m_empnum==0){
        return;
    }
    ofs << endl;
    for (int i=0; i< this->m_empnum; i++){
        ofs << this -> m_emparray[i] -> get_id() << " "
            << this -> m_emparray[i] -> get_name() << " "
            << this -> m_emparray[i] -> get_dept_id() << endl ;

    }

}
WorkerManager::WorkerManager(){
    ifstream ifs;
    ifs.open(FILENAME, ios::in);

    // 没有文件
    if (!ifs.is_open()){
        cout << "当前系统未记录员工，初始化中......" << endl;
        this->m_empnum = 0;
        this -> m_emparray = NULL; 
        this->FileIsEmpty = true;
        ifs.close();
        return;
    }

    // 有文件，但文件中没有内容
    char ch;
    ifs >> ch;
    if (ifs.eof()){
        cout << "当前系统未记录员工，初始化中......" << endl;
        this->m_empnum = 0;
        this -> m_emparray = NULL; 
        this->FileIsEmpty = true;
        ifs.close();
        return;
    }

    string record;
    getline(ifs, record);
    
    if (ifs.eof()){
        cout << "当前系统未记录员工，初始化中......" << endl;
        this->m_empnum = 0;
        this -> m_emparray = NULL; 
        this->FileIsEmpty = true;
        ifs.close();
        return;
    }

    // 有文件，文件中有内容
    cout << "当前系统中记录员工，载入中......" << endl;
    int id,did;
    string name;
    int index = 0;
    int worker_num = this->get_worker_num();

    // 开辟空间
    this -> m_empnum = 0;
    this -> m_emparray = new Worker *[worker_num]; 
    this->FileIsEmpty = false;

    
    Worker *worker = NULL;
    while (ifs >> id && ifs >> name && ifs >>did){
        switch (did)
        {
            case 1:
                worker = new Boss(id, name);
                break;
            case 2:
                worker = new Manager(id, name);
                break;
            case 3:
                worker = new Employer(id, name);
                break;  
            default:
                cout << "记录文件损坏， 请尽快修复" << endl;
                break;
        }
        
        this->m_emparray[index] = worker;
        index ++;
    }
    
    this->m_empnum = index;
    cout << "Done!"<<"共载入" << this->m_empnum << "名员工的信息" << endl;
}


void WorkerManager::show_worker_info(){
    if (this->FileIsEmpty){
        cout << "当前系统中未记录员工信息" << endl;
        return;
    }
    for (int i=0; i<this->m_empnum ; i++){
        this->m_emparray[i]->show_info();
    }
}

void WorkerManager::del_worker(){
    cout<<"请输入要删除的员工编号" <<endl;
    int id;
    cin >> id;
    bool is_exist = false;
    int index = 0;
    for (int i=0; i< this->m_empnum; i++){
        if (this->m_emparray[i]->get_id() == id){
                is_exist = true;
                index = i;
                break;
        }
    }

    if(!is_exist){
        cout << "不存在该编号的职工" << endl;
        return;
    }

    // 元素前移
    this->m_empnum -- ;
    for (int i=index;i<this->m_empnum;i++){
        this->m_emparray[i] = this->m_emparray[i+1];
    }

    this->save();
    cout << "删除成功，当前系统中记录"<< this->m_empnum << "名员工"<<endl;
}



WorkerManager::~WorkerManager(){
    if(this->m_emparray != NULL){
        delete [] this->m_emparray;

    }
}

void WorkerManager::modify_worker(){
    if(this->m_empnum == 0){
        cout << "当前系统中未记录员工信息" << endl;
        return;
    } 
    cout << "请输入要修改的职工编号" << endl;
    int oid;
    cin >> oid;
    bool is_exist = false;
    int index = 0;
    for (int i=0; i<this->m_empnum; i++){
        if (this->m_emparray[i]->get_id() == oid){
            is_exist = true;
            index = i;
        }
    }

    if(!is_exist){
        cout << "不存在该编号的职工" << endl;
        return;
    }
    string name;
    int id,did;
    Worker *worker = NULL;
    cout << "该员工原信息" << endl;
    this->m_emparray[index]->show_info();
    cout << "请输入修改后的姓名" << endl;
    cin >> name;
    cout << "请输入修改后的编号" << endl;
    cin >> id;
    cout << "请输入修改后的部门:1.老板，2.经理，3.普通员工" << endl;
    cin >> did;
    bool input_corret = false;
    while(!input_corret){
        switch (did)
        {
            case 1:
                worker = new Boss(id, name);
                input_corret = true;
                break;
            case 2:
                worker = new Manager(id, name);
                input_corret = true;
                break;
            case 3:
                worker = new Employer(id, name);
                input_corret = true;
                break;
            default:
                cout << "输入错误，请重新输入" << endl;
                break;
        }
    }
    
    this->m_emparray[index] = worker;
    this->save();
    cout << "修改成功，该员工信息更新如下："<< endl;
    this->m_emparray[index]->show_info();
}

void WorkerManager::search_worker_wrapper(){
    if (this->m_empnum == 0){
        cout << "当前系统中未记录员工信息" << endl;
        return;
    }
    cout << "请输入要查找的方式" << endl;
    cout << "1. 按照编号进行查找" << endl;
    cout << "2. 按照姓名进行查找" << endl;

    int select;
    cin >> select;
    if (select == 1){
        cout << "请输入要查找的员工编号" << endl;
        int id;
        cin >>id;
        this->search_worker(id);
    }else{
        cout << "请输入要查找的员工姓名" << endl;
        string name;
        cin >> name;
        this->search_worker(name);
    }

}

void WorkerManager::search_worker(int id){

    bool is_exist = false;
    for (int i=0; i<this->m_empnum; i++){
        if (this->m_emparray[i]->get_id() == id){
            this->m_emparray[i]->show_info();
            is_exist = true;
        }
    }

    if (!is_exist){
        cout << "不存在该编号的职工" << endl;
    }

}

void WorkerManager::search_worker(string name){
    bool is_exist = false;
    for (int i=0; i<this->m_empnum; i++){
        if (this->m_emparray[i]->get_name() == name){
            this->m_emparray[i]->show_info();
            is_exist = true;
        }
    }

    if (!is_exist){
        cout << "不存在该姓名的职工" << endl;
    }
}

void WorkerManager::sort_worker(){
    if (this->m_empnum == 0){
        cout << "当前系统中未记录员工信息" << endl;
        return;
    }

    cout << "请选择排序的方式" << endl;
    cout << "1. 按照编号升序" << endl;
    cout << "2. 按照编号降序" << endl;
    int select;
    cin >> select;
    for (int i = 0; i < m_empnum; i++)
	{
		int minOrMax = i;
		for (int j = i + 1; j < m_empnum; j++)
		{
			if (select == 1) 
			{
				if (m_emparray[minOrMax]->get_id() > m_emparray[j]->get_id())
				{
					minOrMax = j;
				}
			}
			else  
			{
				if (m_emparray[minOrMax]->get_id() < m_emparray[j]->get_id())
				{
					minOrMax = j;
				}
			}
		}

		if (i != minOrMax)
		{
			int temp = m_emparray[i]->get_id();
			m_emparray[i]->set_id(m_emparray[minOrMax]->get_id());
			m_emparray[minOrMax]->set_id(temp);
		}

	}
}

void WorkerManager::reset(){
    this ->m_empnum = 0;
    delete[] this->m_emparray;
    this->FileIsEmpty = true;
    this->save();
}
