#include <iostream>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int size;
	cin >> size;
	int arr[1000000];

	for (int i = 0; i < size; i++) {
		int num;
		cin >> num;
		arr[i] = num;
	}

	int max = arr[0];
	int min = arr[0];

	for (int i = 0; i < size; i++)
	{
		if (arr[i] > max) {
			max = arr[i];
		}
	}
	for (int i = 0; i < size; i++)
	{
		if (arr[i] < min) {
			min = arr[i];
		}
	}

	cout << min << " " << max;

	return 0;
}
