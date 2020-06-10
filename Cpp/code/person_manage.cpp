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
			cout << "��ӭ�´�ʹ��" << endl;
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
	cout << "***** 1�������ϵ�� ******" << endl;
	cout << "***** 2����ʾ��ϵ�� ******" << endl;
	cout << "***** 3��ɾ����ϵ�� ******" << endl;
	cout << "***** 4��������ϵ�� ******" << endl;
	cout << "***** 5���޸���ϵ�� ******" << endl;
	cout << "***** 6�������ϵ�� ******" << endl;
	cout << "***** 0���˳�ͨѶ¼ ******" << endl;
	cout << "������Ҫʹ�õĹ���" << endl;
}

void add_person(Addressbooks * addressbook) {
	string name;
	int sex;
	string sex_string;
	int age;
	string phone;
	string addr;
	cout << "����������" << endl;
	cin >> name;
	cout << "�������Ա�" << endl;
	cout << "��--��1" << endl;
	cout << "Ů--��2" << endl;
	cin >> sex;
	cout << "����������" << endl;
	cin >> age;
	cout << "������绰����" << endl;
	cin >> phone;
	cout << "������סַ" << endl;
	cin >> addr;
	Person person = { name,sex,age,phone,addr };
	addressbook->persons[addressbook->person_num] = person;
	addressbook->person_num++;
	cout << "��ӳɹ�" << endl;
	system("pause");
	system("cls");
}

void show_person(Addressbooks * addressbook) {
	cout << "��ǰ������ϵ��" << addressbook->person_num << "λ" << endl;
	for (int i = 0; i < addressbook->person_num; i++)
	{
		cout << "������" << addressbook->persons[i].m_Name << "\t";
		cout << "�Ա�" << (addressbook->persons[i].m_Sex == 1 ? "��" : "Ů") << "\t";
		cout << "���䣺" << addressbook->persons[i].m_Age << "\t";
		cout << "�绰��" << addressbook->persons[i].m_Phone << "\t";
		cout << "סַ��" << addressbook->persons[i].m_Addr << endl;
	}
	system("pause");
	system("cls");
}

void delete_person(Addressbooks * addressbook) {
	string name;
	cout << "������Ҫɾ����ϵ�˵�����"<<endl;
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
	cout << "ɾ���ɹ�" << endl;
	system("pause");
	system("cls");
}

void search_person(Addressbooks * addressbook) {
	string name;
	cout << "������Ҫ������ϵ�˵�����" << endl;
	cin >> name;
	int i = 0;
	for (i = 0; i < addressbook->person_num; i++) {
		if (addressbook->persons[i].m_Name == name) {
			break;
		}
	}
	if (i == addressbook->person_num) {
		cout << "���޴���" << endl;
	}
	else {
		cout << "������" << addressbook->persons[i].m_Name << "\t";
		cout << "�Ա�" << (addressbook->persons[i].m_Sex == 1 ? "��" : "Ů") << "\t";
		cout << "���䣺" << addressbook->persons[i].m_Age << "\t";
		cout << "�绰��" << addressbook->persons[i].m_Phone << "\t";
		cout << "סַ��" << addressbook->persons[i].m_Addr << endl;
	}
	system("pause");
	system("cls");
}

void clear_person(Addressbooks * addressbook) {
	addressbook->person_num = 0;
	cout << "���ͨѶ¼�ɹ�" << endl;
	system("pause");
	system("cls");
}

void config_person(Addressbooks * addressbook) {
	string name;
	cout << "������Ҫ�޸���ϵ�˵�����" << endl;
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
		cout << "������Ҫ�޸ĵ�����:" << endl;
		cout<<"1.����" << "\t2.�Ա�" << "\t3.����" << "\t4.�绰" << "\t5.סַ" << "\t6.�˳��޸�" << endl;
		cin >> select;
		switch (select)
		{
		case 0:
			break;
		case 1:
			cout << "����������" << endl;
			cin >> name;
			addressbook->persons[i].m_Name = name;
			count++;
			break;
		case 2:
			cout << "�������Ա�" << endl;
			cin >> sex;
			addressbook->persons[i].m_Sex = sex;
			count++;
			break;
		case 3:
			cout << "����������" << endl;
			cin >> age;
			addressbook->persons[i].m_Age = age;
			count++;
			break;
		case 4:
			cout << "������绰" << endl;
			cin >> phone;
			addressbook->persons[i].m_Phone = phone;
			count++;
			break;
		case 5:
			cout << "������סַ" << endl;
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