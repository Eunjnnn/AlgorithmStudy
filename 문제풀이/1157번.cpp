#include <stdio.h>
#include <string.h>

int main() {
	char string[1000001], c = '?';
	int arr[26]= { 0 };
	int i, max=0;
	
	fgets(string, sizeof(string), stdin);
	
	for(i = 0; string[i] != '\0'; i++) {
		if('a' <= string[i])
			string[i] = string[i] - 32;
		arr[string[i] - 'A'] ++;
	}
		
	for(i = 0; i<26; i++) {
		if(max < arr[i]) {
			max = arr[i];
			c = 'A' + i;
		} else if(max == arr[i]) {
			c = '?';
		}
	}
	
	printf("%c", c);
	
	return 0;
}
