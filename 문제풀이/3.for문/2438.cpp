#include <iostream>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int a;
	cin >> a;

	for (int i = 1; i <= a; i++) {
		for (int b = 1; b <= i; b++) {
			cout << "*";
		}
		cout << '\n';
	}

	return 0;
}
