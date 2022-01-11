#include <iostream>

using namespace std;

int main() {
	int N;
	double arr[1000];
	cin >> N;
	int score;
	int max = 0;

	for (int i = 0; i < N; i++) {
		cin >> score;
		arr[i] = score;
		if (max < arr[i]) {
			max = arr[i];
		}
	}
	double sum = 0;

	for (int i = 0; i < N; i++) {
		arr[i] = arr[i] / max * 100;
		sum += arr[i];
	}

	cout << sum / N << endl;


	return 0;
}
