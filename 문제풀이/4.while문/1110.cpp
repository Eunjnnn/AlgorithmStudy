#include <iostream>

using namespace std;


int main() {
	int N;
	int a = 0;
	cin >> N;
	int num = N;
	int first, second;


	 do {
		first = N / 10;
		second = N % 10;
		int b = first + second;
		N = second * 10 + b % 10;
		a++;
	 } while (N != num);

	cout << a;

	return 0;
}
