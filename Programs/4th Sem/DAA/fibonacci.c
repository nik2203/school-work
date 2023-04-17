#include <stdio.h>
#include <stdlib.h>
long long operation(int n)
{
    // Write your code here
    if (n <= 3)
        return n;
    long long *a = (long long *)calloc(13, sizeof(long long));
    a[0] = 1;
    a[1] = 2;
    a[2] = 3;
    for (int i = 3; i < n; i++)
    {
        a[i] = a[i - 1] * a[i - 3];
    }
    return a[n - 1];
}

// Driver's code
int main()
{
    int n;
    scanf("%d", &n);
    printf("%lld\n", operation(n));
    return 0;
}