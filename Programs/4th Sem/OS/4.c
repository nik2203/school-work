#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <fnmatch.h>


int main(int argc, char *argv[]) {
    DIR *dir;
    struct dirent *ent;
    char *dirname, *pattern;
    if (argc != 3) {
        printf("Usage: %s <directory> <filename>\n", argv[0]);
        return 1;
    }
    dirname = argv[1];
    pattern = argv[2];
    dir = opendir(dirname);
    if (dir == NULL) {
        printf("Could not open directory '%s'\n", dirname);
        return 1;
    }
    while ((ent = readdir(dir)) != NULL) {
        if (fnmatch(pattern, ent->d_name, 0) == 0) {
            printf("%s\n",ent->d_name);
        }
    }
    closedir(dir);
    return 0;
}

