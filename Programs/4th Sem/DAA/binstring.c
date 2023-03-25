#include <stdio.h>
#include <string.h>

int min_binary_string(char *s) {
    int b=0,e=(strlen(s)-1);
    int res=strlen(s);
    while((b<e)&&(s[b]!=s[e])){
        b++;
        e--;
        res--;
        res--;
    }
    return res;
}

int main() {
    char s[100];
    scanf("%s", s);
    printf("%d", min_binary_string(s));
    return 0;
}
