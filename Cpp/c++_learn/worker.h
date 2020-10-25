#include <iostream>

using namespace std;

class Worker
{
public:

    virtual void show_info() = 0;

    virtual string get_dept_name()=0;

    int get_id(){
        return this->m_id;
    }

    string get_name(){
        return this->m_name;
    }
    
    int get_dept_id(){
        return this->m_dept_id;
    }

protected:
    int m_id;
    string m_name;
    int m_dept_id;
};


class Employer:public Worker{
public:
    void show_info();
    string get_dept_name();
    Employer(int m_id, string m_name);
};


class Manager:public Worker{
public:
    void show_info();
    string get_dept_name();
    Manager(int m_id, string m_name);

};


class Boss:public Worker{
public:
    void show_info();
    string get_dept_name();
    Boss(int m_id, string m_name);

};
