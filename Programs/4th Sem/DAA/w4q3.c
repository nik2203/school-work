#include <stdio.h>
#include <stdio.h>



void operation(int n, int (*graph)[n])
{
    int parent[n], r[n];
    for (int i = 0; i < n; i++)
    {
        parent[i] = i;
        r[i] = 0;
    }
    int tw = 0;
    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = i - 1; j >= 0; j--)
        {
            if (graph[i][j] > graph[j][i])
            {
                int temp = graph[i][j];
                graph[i][j] = graph[j][i];
                graph[j][i] = temp;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (graph[i][j] > 0)
            {
                int root_i = i, root_j = j;
                while (parent[root_i] != root_i)
                {
                    root_i = parent[root_i];
                }
                while (parent[root_j] != root_j)
                {
                    root_j = parent[root_j];
                }
                if (root_i != root_j)
                {
                    tw += graph[i][j];
                    if (r[root_i] > r[root_j])
                    {
                        parent[root_j] = root_i;
                    }
                    else
                    {
                        parent[root_i] = root_j;
                        if (r[root_i] == r[root_j])
                        {
                            r[root_j]++;
                        }
                    }
                }
            }
        }
    }
    printf("%d\n", tw);
}


void main()
{
    int n, i, j, edges, e, src, dest, len;
    scanf("%d", &n);
    int graph[n][n];
    scanf("%d", &edges);
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            graph[i][j] = 0;
        }
    }
    for (e = 0; e < edges; e++)
    {
        scanf("%d %d %d", &src, &dest, &len);
        graph[src - 1][dest - 1] = len;
        graph[dest - 1][src - 1] = len;
    }
    operation(n, graph);
}