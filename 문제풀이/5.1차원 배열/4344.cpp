#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	int C;
	int arr[1000];
	cin >> C;

	for (int i = 0; i < C; i++) {
		int N;
		cin >> N;
		int sum = 0;
		for (int j = 0; j < N; j++) {
			int score;
			cin >> score;
			arr[j] = score;
			sum += arr[j];
		}
		int ave = sum / N;
		int count = 0;
		for (int k = 0; k < N; k++) {
			if (arr[k] > ave) {
				count++;
			}
 		}
		double n = (double)count / N;
		printf("%.3lf", n * 100);
		cout << "%" << endl;
	}

	return 0;
}
