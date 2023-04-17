#include <stdio.h>
#include <stdlib.h>


void solution(int src, int n, int path[n][n])
{
    int dist[n][n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            dist[i][j] = path[i][j];
        }
    }
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (dist[i][k] != 1000 && dist[k][j] != 1000 &&
                    dist[i][k] + dist[k][j] < dist[i][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        // printf("%d\n", dist[src][i]);
        if (i == src)
        {
            printf("0\n");
            continue;
        }
        if (dist[src][i] >= 500)
        {
            printf("-1\n");
            continue;
        }
        int count = 0;
        for (int j = 0; j < n; j++)
        {
            if (j != src && j != i && dist[src][j] + dist[j][i] == dist[src][i])
            {
                count++;
            }
        }
        printf("%d\n", count);
    }
}

void main()
{
    // driver’s code
    int n;
    int src;
    scanf("%d", &n);
    scanf("%d", &src);
    int(*adj)[n] = malloc(sizeof(int) * n * n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &adj[i][j]);
        }
    }
    solution(src, n, adj);
}