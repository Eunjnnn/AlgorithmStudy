#include<iostream>
#include<cstring>
using namespace std;

int main() {
	char input[80];
	int sum = 0;
	int correct = 0;
	int loopTime = 0;
	int time;

	cin >> time;

	while (time > loopTime) {
		cin >> input;

		for (int i = 0; i < strlen(input); i++) {
			if (input[i] == 'O') {
				correct++;
				sum = sum + correct;
			}
			else {
				correct = 0;
			}
		}
		cout << sum << endl;
		sum = 0;
		correct = 0;
		loopTime++;
	}
	return 0;
}
