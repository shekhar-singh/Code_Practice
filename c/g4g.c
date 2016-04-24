#include<stdio.h>

int main()
{


}
int myatoi(char str[])
{
	int retval = 0;
	int i = 0;

	while(str[i] != '\0')
		{
		int digit = str[i] - '0';
		retval = 10 * retval + digit;
		i++;
		}

	return retval;
}
