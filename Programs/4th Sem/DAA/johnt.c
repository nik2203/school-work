#include <stdio.h>
#include <stdlib.h>

// Function to print the permutation
void print_perm(int n, int *perm)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", perm[i]);
    }
    printf("\n");
}

// Function to swap two adjacent elements of the permutation
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Johnson-Trotter algorithm for generating permutations
void jt(int n)
{
    int perm[n];
    int dir[n];
    for (int i = 0; i < n; i++)
    {
        perm[i] = i + 1;
        dir[i] = -1;
    }
    print_perm(n, perm);
    while (1)
    {
        int k = -1, j = -1;
        for (int i = 0; i < n; i++)
        {
            if ((dir[i] == -1 && i > 0 && perm[i] > perm[i - 1]) ||
                (dir[i] == 1 && i < n - 1 && perm[i] > perm[i + 1]))
            {
                if (perm[i] > k)
                {
                    k = perm[i];
                    j = i;
                }
            }
        }
        if (k == -1)
            break;
        if (dir[j] == -1)
        {
            swap(&perm[j], &perm[j - 1]);
            swap(&dir[j], &dir[j - 1]);
            j--;
        }
        else
        {
            swap(&perm[j], &perm[j + 1]);
            swap(&dir[j], &dir[j + 1]);
            j++;
        }
        for (int i = 0; i < n; i++)
        {
            if (perm[i] > k)
            {
                dir[i] = -dir[i];
            }
        }
        print_perm(n, perm);
    }
}

int main()
{
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    jt(n);
    return 0;
}
