#include <stdio.h>

int count = 0;

int div(int a) {
	int i;
	int first, second, third;

	for(i = 1; i<= a;i++) {
		if(i<100) {
			count++;
		}
		else if(i>=100 && i<1000){
			third = i / 100;
			second = (i-third*100) / 10;
			first = i-third*100-second*10;
			if(first-second==second-third) {
				count++;
			}
		}
	}
}

int main() {
	int num;
	scanf("%d", &num);

	div(num);

	printf("%d", count);

	return 0;
}
