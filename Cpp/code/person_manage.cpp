#include <iostream>
#include <string>
using namespace std;
\
#define MAX 1000
struct Person
{
	string m_Name;
	int m_Sex; 
	int m_Age;
	string m_Phone; 
	string m_Addr;
};
struct Addressbooks {
	struct Person persons[MAX];
	int person_num;
};

void show_menu();
void add_person(Addressbooks * addressbook);
void show_person(Addressbooks * addressbook);
void delete_person(Addressbooks * addressbook);
void search_person(Addressbooks * addressbook);
void clear_person(Addressbooks * addressbook);
void config_person(Addressbooks * addressbook);
int main() {
	int select = -1;
	Addressbooks addressbook;
	addressbook.person_num = 0;
	while (1) {
		show_menu();
		cin >> select;
		switch (select)
		{
		case 0:
			cout << "欢迎下次使用" << endl;
			system("pause");
			return 0;
		case 1:
			add_person(&addressbook);
			break;
		case 2:
			show_person(&addressbook);
			break;
		case 3:
			delete_person(&addressbook);
			break;
		case 4:
			search_person(&addressbook);
			break;
		case 5:
			config_person(&addressbook);
			break;
		case 6:
			clear_person(&addressbook);
			break;
		}
	}
	system("pause");
}

void show_menu() {
	cout << "************" << endl;
	cout << "***** 1、添加联系人 ******" << endl;
	cout << "***** 2、显示联系人 ******" << endl;
	cout << "***** 3、删除联系人 ******" << endl;
	cout << "***** 4、查找联系人 ******" << endl;
	cout << "***** 5、修改联系人 ******" << endl;
	cout << "***** 6、清空联系人 ******" << endl;
	cout << "***** 0、退出通讯录 ******" << endl;
	cout << "请输入要使用的功能" << endl;
}

void add_person(Addressbooks * addressbook) {
	string name;
	int sex;
	string sex_string;
	int age;
	string phone;
	string addr;
	cout << "请输入姓名" << endl;
	cin >> name;
	cout << "请输入性别" << endl;
	cout << "男--》1" << endl;
	cout << "女--》2" << endl;
	cin >> sex;
	cout << "请输入年龄" << endl;
	cin >> age;
	cout << "请输入电话号码" << endl;
	cin >> phone;
	cout << "请输入住址" << endl;
	cin >> addr;
	Person person = { name,sex,age,phone,addr };
	addressbook->persons[addressbook->person_num] = person;
	addressbook->person_num++;
	cout << "添加成功" << endl;
	system("pause");
	system("cls");
}

void show_person(Addressbooks * addressbook) {
	cout << "当前共有联系人" << addressbook->person_num << "位" << endl;
	for (int i = 0; i < addressbook->person_num; i++)
	{
		cout << "姓名：" << addressbook->persons[i].m_Name << "\t";
		cout << "性别：" << (addressbook->persons[i].m_Sex == 1 ? "男" : "女") << "\t";
		cout << "年龄：" << addressbook->persons[i].m_Age << "\t";
		cout << "电话：" << addressbook->persons[i].m_Phone << "\t";
		cout << "住址：" << addressbook->persons[i].m_Addr << endl;
	}
	system("pause");
	system("cls");
}

void delete_person(Addressbooks * addressbook) {
	string name;
	cout << "请输入要删除联系人的姓名"<<endl;
	cin >> name;
	int i = 0;
	for (i = 0; i < addressbook->person_num; i++) {
		if (addressbook->persons[i].m_Name == name) {
			break;
		}
	}
	for (int j = i; j < addressbook->person_num-1; j++) {
		addressbook->persons[j] = addressbook->persons[j + 1];
	}
	addressbook->person_num--;
	cout << "删除成功" << endl;
	system("pause");
	system("cls");
}

void search_person(Addressbooks * addressbook) {
	string name;
	cout << "请输入要查找联系人的姓名" << endl;
	cin >> name;
	int i = 0;
	for (i = 0; i < addressbook->person_num; i++) {
		if (addressbook->persons[i].m_Name == name) {
			break;
		}
	}
	if (i == addressbook->person_num) {
		cout << "查无此人" << endl;
	}
	else {
		cout << "姓名：" << addressbook->persons[i].m_Name << "\t";
		cout << "性别：" << (addressbook->persons[i].m_Sex == 1 ? "男" : "女") << "\t";
		cout << "年龄：" << addressbook->persons[i].m_Age << "\t";
		cout << "电话：" << addressbook->persons[i].m_Phone << "\t";
		cout << "住址：" << addressbook->persons[i].m_Addr << endl;
	}
	system("pause");
	system("cls");
}

void clear_person(Addressbooks * addressbook) {
	addressbook->person_num = 0;
	cout << "清空通讯录成功" << endl;
	system("pause");
	system("cls");
}

void config_person(Addressbooks * addressbook) {
	string name;
	cout << "请输入要修改联系人的姓名" << endl;
	cin >> name;
	int i = 0;
	for (i = 0; i < addressbook->person_num; i++) {
		if (addressbook->persons[i].m_Name == name) {
			break;
		}
	}
	int count = 0;
	int select;
	string phone;
	string addr;
	int sex;
	int age;
	while (count<=5) {
		cout << "请输入要修改的内容:" << endl;
		cout<<"1.姓名" << "\t2.性别" << "\t3.年龄" << "\t4.电话" << "\t5.住址" << "\t6.退出修改" << endl;
		cin >> select;
		switch (select)
		{
		case 0:
			break;
		case 1:
			cout << "请输入姓名" << endl;
			cin >> name;
			addressbook->persons[i].m_Name = name;
			count++;
			break;
		case 2:
			cout << "请输入性别" << endl;
			cin >> sex;
			addressbook->persons[i].m_Sex = sex;
			count++;
			break;
		case 3:
			cout << "请输入年龄" << endl;
			cin >> age;
			addressbook->persons[i].m_Age = age;
			count++;
			break;
		case 4:
			cout << "请输入电话" << endl;
			cin >> phone;
			addressbook->persons[i].m_Phone = phone;
			count++;
			break;
		case 5:
			cout << "请输入住址" << endl;
			cin >> addr;
			addressbook->persons[i].m_Addr = addr;
			count++;
			break;
		case 6:
			count = 6;
			break;
		default:
			break;
		}
	}
	system("pause");
	system("cls");
}