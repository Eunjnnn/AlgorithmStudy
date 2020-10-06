#include <stdio.h> 

int main(void) {
	int testNum, R, i , k;
	char string[20];
	
	scanf("%d", &testNum);
	
	for(i = 0;i < testNum; i++) {
		scanf("%d %s", &R, string);
		for(k = 0; k < R; k++) {
			printf("%s", string[k]);
		}
	}
	
	return 0;
}
