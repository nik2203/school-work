#include <stdio.h>
#include <string.h>
#include <conio.h>


void shift(char pattern[], int m, int table[])
{
    for (int i = 0; i < 256; i++)
    {
        table[i] = m;
    }
    for (int i = 0; i < m - 1; i++)
    {
        table[(int)pattern[i]] = m - i - 1;
    }
}


void operation(char text[], char pattern[])
{
    int n = strlen(text);
    int m = strlen(pattern);
    int table[256];
    shift(pattern, m, table);
    int count = 0;
    for (int i = m - 1; i < n;)
    {
        int j = m - 1;
        while (j >= 0 && pattern[j] == text[i - m + 1 + j])
        {
            j--;
        }
        if (j == -1)
        {
            printf("%d ", i - m + 2);
            count++;
            if (count == 2 || m == n)
            {
                return;
            }
            i++;
        }
        else
        {
            i += table[(int)text[i]];
        }
    }
    printf("-1");
}



int main()
{
    char text[500], pattern[500];
    gets(text);
    gets(pattern);
    operation(text, pattern);
    return 0;
}