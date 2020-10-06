#include <stdio.h> 
#include <string.h>

int main(void) {
	int testNum, R, i , k, j;
	char string[21];
	
	scanf("%d", &testNum);
	
	for(i = 0;i < testNum; i++) {
		scanf("%d %s", &R, string);
		for(k = 0; k< strlen(string); k++) {
			for(j = 0; j<R; j++) {
				printf("%c", string[k]);
			}
		}
		printf("\n");
	}
	
	return 0;
}
