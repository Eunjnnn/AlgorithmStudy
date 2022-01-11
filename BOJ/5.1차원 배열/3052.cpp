#include <iostream>

using namespace std;

int main() {
	int num;
	int b = 42;
	int arr[10];
	int count = 0;

	for (int i = 0; i < 10; i++) {
		cin >> num;
		arr[i] = num % b;
		for (int j = 0; j <= i; j++) {
			if (arr[j] == arr[i] && i != j) {
				count--;
				break;
			}
		}
		count++;
	}

	cout << count;

	return 0;
}
