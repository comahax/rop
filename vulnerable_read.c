#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

int fd = 0;

int vulnerable_code()
{
	char temp[500];
	read(STDIN_FILENO, temp, 512 + 100);
	return 0;
}

int main(int argc, char **argv)
{
	vulnerable_code();
	write(STDOUT_FILENO, "Hello World!\n", 13);
	return 0;
}
