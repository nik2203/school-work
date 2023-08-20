#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <dirent.h>
#include <time.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s directory date\n", argv[0]);
        return 1;
    }

    char* directory = argv[1];
    char* date_str = argv[2];

    struct tm date;
    if (strptime(date_str, "%Y-%m-%d", &date) == NULL) {
        fprintf(stderr, "Error: invalid date format\n");
        return 1;
    }
    time_t timestamp = mktime(&date);

    DIR* dir = opendir(directory);
    if (dir == NULL) {
        perror("Error");
        return 1;
    }

    struct dirent* entry;
    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        char path[1024];
        snprintf(path, sizeof(path), "%s/%s", directory, entry->d_name);

        struct stat status;
        if (stat(path, &status) != 0) {
            perror("Error");
            continue;
        }

        if (status.st_mtime > timestamp) {
            off_t old_size = status.st_size;
            off_t new_size = old_size / 2;

            int fd = open(path, O_WRONLY | O_TRUNC);
            if (fd == -1) {
                perror("Error");
                continue;
            }

            if (ftruncate(fd, new_size) != 0) {
                perror("Error");
            } else {
                printf("Truncated %s from %ld bytes to %ld bytes\n", path, old_size, new_size);
            }

            close(fd);
        }
    }

    closedir(dir);

    return 0;
}
