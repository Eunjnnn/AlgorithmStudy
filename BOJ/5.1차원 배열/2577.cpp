#include <iostream>

using namespace std;

int main() {
	int A, B, C, i = 0;
	int arr[10] = { 0, };
	cin >> A >> B >> C;
	int final = A * B * C;

	while (final > 0) {
		int rest;
		rest = final % 10;
		final = final / 10;
		arr[rest]++;
	}

	for (int k = 0; k < 10; k++) {
		cout << arr[k] << endl;
	}

	return 0;
}
