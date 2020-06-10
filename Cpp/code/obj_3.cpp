#include <iostream>
using namespace std;
#include <string>

class Visit_friend;
class roommate{
public:
    void visit(Room &room);
};
class Room {
    /*类做友元*/
	friend class Visit_friend;
    /*全局函数做友元*/
	friend void visit(Room &room);
    /*成员函数做友元*/
    friend void roommate::visit(Room &room);
public:
	string sittingroom;

	Room(string sittingroom_name, string bedroom_name) :sittingroom(sittingroom_name), bedroom(bedroom_name) {}
private:
	string bedroom;

};

/*成员函数做友元*/
void roommate::visit(Room &room){
    cout << "i am visting " << room.sittingroom << endl;
	cout << "i am visting " << room.bedroom << endl;
}
class Visit_friend {
public:
	void vist(Room &firendroom) {
		cout << "i am visting " << firendroom.sittingroom << endl;
		cout << "i am visting " << firendroom.bedroom << endl;
	}
};

void visit(Room &room) {
	cout << "i am visting " << room.sittingroom << endl;
	cout << "i am visting " << room.bedroom << endl;
}

int main() {
	Room room = Room("sittingroom", "bedroom");
	Visit_friend visit_friend;
	cout << "---类做友元----" << endl;
	visit_friend.vist(room);
	cout << "---全局函数做友元----" << endl;
	visit(room);

}