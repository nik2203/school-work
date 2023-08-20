#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <dirent.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#include <pwd.h>
#include <grp.h>

int main(int argc, char* argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s directory date new_owner\n", argv[0]);
        return 1;
    }

    char* directory = argv[1];
    char* date_str = argv[2];
    char* owner_str = argv[3];

    struct tm date;
    if (strptime(date_str, "%Y-%m-%d", &date) == NULL) {
        fprintf(stderr, "Error: invalid date format\n");
        return 1;
    }
    time_t timestamp = mktime(&date);

    struct passwd *owner = getpwnam(owner_str);
    if (owner == NULL) {
        fprintf(stderr, "Error: invalid owner username\n");
        return 1;
    }
    uid_t owner_id = owner->pw_uid;
    gid_t owner_group = owner->pw_gid;

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
            if (chown(path, owner_id, owner_group) != 0) {
                perror("Error");
            } else {
                printf("Changed ownership of %s to %s\n", path, owner_str);
            }
        }
    }

    closedir(dir);

    return 0;
}
