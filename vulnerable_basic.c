#include <stdio.h>
#include <string.h>

void vulnerable_code(char *str)
{
	char temp[500];
	strcpy(temp, str);
	printf("%s\n", temp);
}

int main(int argc, char **argv)
{
	vulnerable_code(argv[1]);
	return 0;
}
