#include <iostream>
using namespace std;
#include "worker.h"

void Employer::show_info(){
    cout << "职工编号：" << this->m_id
        << "\t职工姓名：" << this->m_name
        << "\t岗位：" << this->get_dept_name()
        << "\t岗位职责：完成经理交给的任务"
        << endl;
}

string Employer::get_dept_name(){
    string name = "普通员工";
    return name;
}


Employer::Employer(int m_id, string m_name)
{
    this->m_id = m_id;
    this->m_name = m_name;
    this->m_dept_id = 3;
}


void Manager::show_info(){
    cout << "职工编号：" << this->m_id
        << "\t职工姓名：" << this->m_name
        << "\t岗位：" << this->get_dept_name()
        << "\t岗位职责：完成老板交给的任务，并下发任务给员工" 
        << endl;
}

string Manager::get_dept_name(){
    return string("经理");
}

Manager::Manager(int m_id, string m_name){
    this->m_id = m_id;
    this->m_name = m_name;
    this->m_dept_id = 2;
}


void Boss::show_info(){
    cout << "职工编号：" << this->m_id
        << "\t职工姓名：" << this->m_name
        << "\t岗位：" << this->get_dept_name()
        << "\t岗位职责：统筹公司的所有事务" 
        << endl;
}

string Boss::get_dept_name(){
    return string("老板");
}

Boss::Boss(int m_id, string m_name){
    this->m_id = m_id;
    this->m_name = m_name;
    this->m_dept_id = 1;
}


