#include <iostream>

using namespace std;

int main() {
	int fixed_cost, var_cost, cost, point;

	cin >> fixed_cost >> var_cost >> cost;

	if (cost - var_cost > 0) {
		point = fixed_cost / (cost - var_cost) + 1;
		cout << point;
	}
	else {
		cout << "-1";
	}
	return 0;
}
