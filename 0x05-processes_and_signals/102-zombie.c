#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 *infinite_while - infinite loop
 *Return: 0 for success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 *main - main function
 *Return: 0 for success
 */

int main(void)
{
	int i = 0;
	pid_t child_pid;

	for (; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
		}
	}
	infinite_while();
	return (0);
}
