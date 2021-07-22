#include <stdio.h>

int swap(int n) {
	int a, b, c;
	a = n/100;
	b = (n - 100*a) / 10;
	c = n - 100*a - 10*b;
	
	return c*100 + b * 10 + a;
}

int main() {
	int num1, num2;
	
	scanf("%d %d", &num1, &num2);
	
	if(swap(num1) > swap(num2)) printf("%d", swap(num1));
	else printf("%d", swap(num2));
	
	return 0;
}
