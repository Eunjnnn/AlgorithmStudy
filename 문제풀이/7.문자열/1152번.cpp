#include <stdio.h>
#include <string.h>

int main() {
	char string[1000000];
	int i, count=0, spaceNum = 0;
	
	gets(string);
	
	for(i = 0; i< strlen(string) - 1; i++) {
		if(string[i] == ' ') spaceNum++;
	}
	
	count = spaceNum+1;
	if(string[0] == ' ') count--;
	if(string[sizeof(string) - 1] == ' ') count--;
	
	printf("%d", count);
	return 0;
}
