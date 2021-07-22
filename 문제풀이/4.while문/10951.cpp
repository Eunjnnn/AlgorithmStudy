#include <iostream>

using namespace std;


int main() {


	int a=1, b=1;

	while (a != 0 && b != 0) {
		cin >> a >> b;
		if (cin.eof()) {
			break;
		}
		cout << a + b << endl;
	}

	return 0;
}
