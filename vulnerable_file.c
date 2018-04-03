#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

int fd = 0;

int vulnerable_code()
{
	char temp[500];
	//read(STDIN_FILENO, temp, 512 + 12);
	read(fd, temp, 512 + 20);
	printf("%s\n", temp);
	return 0;
}

int main(int argc, char **argv)
{
	fd = open("test.txt", O_RDONLY);
	vulnerable_code();
	write(STDOUT_FILENO, "Hello World!\n", 13);
	close(fd);
	return 0;
}
