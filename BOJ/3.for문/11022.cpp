#include <iostream>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int a;
	cin >> a;

	for (int i = 1; i <= a; i++) {
		int num1, num2;
		cin >> num1 >> num2;
		cout << "Case #" << i << ": " << num1 << " + " << num2 << " = " << num1 + num2 << '\n';
	}

	return 0;
}
