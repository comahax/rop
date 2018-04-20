#include <stdio.h>
#include <string.h>
#include <unistd.h>

int vunerable_func(char *arg)
{
	char str[500];
	strcpy(str, arg);
	printf("%s\n", str);
}


int main(int argc, char **arg)
{
	vunerable_func(arg[1]);
	return 0;
}
