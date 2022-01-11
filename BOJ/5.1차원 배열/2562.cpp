#include <iostream>

using namespace std;

int main() {
	int arr[10];
	int num;
	int max = 0;
	int max_num = 0;

	for (int i = 1; i <= 9; i++) {
		cin >> num;
		arr[i] = num;

		if (arr[i] < 100) {
			if (arr[i] > max) {
				max = arr[i];
				max_num = i;
			}
		}
	}

	cout << max << endl << max_num;

	return 0;
}
