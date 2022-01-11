#include <stdio.h>

int Quadrant(int x, int y) {
	if(x>0 && y > 0){
		return 1;
	}
	else if(x<0 && y > 0){
		return 2;
	}
	else if(x<0 && y < 0){
		return 3;
	}
	else{
		return 4;
	}
}

int main() {
	int a, b;

	scanf("%d %d", &a, &b);

	printf("%d", Quadrant(a,b));

	return 0;
}
