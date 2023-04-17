#include <stdio.h>
#include <stdlib.h>
void solution(int src, int n, int path[n][n], int dist)
{
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (path[i][k] != 1000 && path[k][j] != 1000 &&
                    path[i][k] + path[k][j] < path[i][j])
                {
                    path[i][j] = path[i][k] + path[k][j];
                }
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (path[src][i] <= dist)
        {
            printf("%d\n", i);
            continue;
        }
    }
}

void main()
{
    // Driver's Code
    int n;
    int src;
    int dist;
    scanf("%d", &n);
    scanf("%d", &src);
    scanf("%d", &dist);
    int(*adj)[n] = malloc(sizeof(int) * n * n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &adj[i][j]);
        }
    }
    solution(src, n, adj, dist);
}