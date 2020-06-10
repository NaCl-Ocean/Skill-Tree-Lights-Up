#include <iostream>
using namespace std;
#include <string>


class Cube
{
private:
	int * h;
	int l;

public:
	Cube(int h_input, int l_input) {
		h = new int(h_input);
		l = l_input;
	}
	~Cube() {
		if (h != NULL) {
			delete h;
			h = NULL;
		}
	}
};


void test() {
	Cube cube_1 = Cube(10, 20);
	Cube cube_2 = Cube(cube_1);
}

int main() {
	test();
}