#include <stdio.h>

int main()
{
	char line[100];
	int n;

	while(1)
		{
		printf("type a number:\n");
		if(getline(line, 100) == EOF)
			break;
		n = myatoi(line);
		printf("you typed %d\n", n);
		}

	return 0;
}

