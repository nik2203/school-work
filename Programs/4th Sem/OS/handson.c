#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
	int x, y;
	printf("Enter values for x and y\n");
	scanf("%d", &x);
	scanf("%d", &y);
	char x_str[16], y_str[16];
	sprintf(x_str, "%d", x);
	sprintf(y_str, "%d", y);
	char *args[] = {"./product", x_str, y_str, NULL};
	execvp(args[0], args);
}