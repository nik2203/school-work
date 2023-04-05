#include <stdio.h>
#include <string.h>


#define MAX(x, y) (((x) > (y)) ? (x) : (y))

void bad_char_shift(char *pattern, int m, int *bad_char)
{
    int i;
    for (i = 0; i < 256; i++)
    {
        bad_char[i] = m;
    }
    for (i = 0; i < m - 1; i++)
    {
        bad_char[(int)pattern[i]] = m - i - 1;
    }
}

void good_suffix_shift(char *pattern, int m, int *good_suffix)
{
    int i, j;
    int suff[m];
    suff[m - 1] = m;
    j = m - 1;
    for (i = m - 2; i >= 0; i--)
    {
        while (j < m - 1 && pattern[j] != pattern[i])
        {
            j = suff[j + 1] - 1;
        }
        if (pattern[j] == pattern[i])
        {
            j--;
        }
        suff[i] = j + 1;
    }
    for (i = 0; i < m; i++)
    {
        good_suffix[i] = m - suff[i];
    }
}


void operation(char *pattern, char *text, int *gscore, int *bscore)
{
    int m = strlen(pattern);
    int n = strlen(text);
    int i, j;
    int bad_char[256];
    int good_suffix[m];
    bad_char_shift(pattern, m, bad_char);
    good_suffix_shift(pattern, m, good_suffix);
    i = m - 1;
    *gscore = 0;
    *bscore = 0;
    while (i < n)
    {
        j = m - 1;
        while (text[i] == pattern[j])
        {
            if (j == 0)
            {
                (*gscore)++;
                return;
            }
            (*gscore)++;
            i--;
            j--;
        }
        (*bscore)++;
        i += MAX(bad_char[(int)text[i]], good_suffix[j]);
    }
    if (j == m - 1)
    {
        *gscore = 0;
        *bscore = m;
    }
}


int main()
{
    char text[500], pattern[500];
    int gscore = 0, bscore = 0;
    gets(text);
    gets(pattern);
    operation(pattern, text, &gscore, &bscore);
    printf("%d %d", gscore, bscore);
    return 0;
}