#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <dirent.h>
#include <time.h>
#include <string.h>

int main(int argc, char* argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s directory date new_permission\n", argv[0]);
        return 1;
    }

    char* directory = argv[1];
    char* date_str = argv[2];
    char* permission_str = argv[3];

    struct tm date;
    if (strptime(date_str, "%Y-%m-%d", &date) == NULL) {
        fprintf(stderr, "Error: invalid date format\n");
        return 1;
    }
    time_t timestamp = mktime(&date);

    mode_t new_permission = strtol(permission_str, NULL, 8);

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
            if (chmod(path, new_permission) != 0) {
                perror("Error");
            } else {
                printf("Changed permission of %s to %o\n", path, new_permission);
            }
        }
    }

    closedir(dir);

    return 0;
}
