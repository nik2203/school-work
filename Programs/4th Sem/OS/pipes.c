#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int fd[2];
    pid_t pid;

    if (pipe(fd) == -1) {
        fprintf(stderr, "Pipe failed");
        return 1;
    }

    pid = fork();

    if (pid < 0) {
        fprintf(stderr, "Fork failed");
        return 1;
    }
    else if (pid == 0) {
        close(fd[1]);
        char input_str[100];
        read(fd[0], input_str, 100);

        int length = strlen(input_str);
        for (int i = 0; i < length / 2; i++) {
            char temp = input_str[i];
            input_str[i] = input_str[length - i - 1];
            input_str[length - i - 1] = temp;
        }

        printf("Reversed string: %s\n", input_str);
        close(fd[0]);
    }
    else {
        close(fd[0]);
        char output_str[100];
        printf("Enter a string: ");
        fgets(output_str, 100, stdin);

        write(fd[1], output_str, strlen(output_str) + 1);
        close(fd[1]);
        wait(NULL);
    }

    return 0;
}
