#include <stdio.h>
#include <stdbool.h>

#define MAX_NODES 100

#define INF 1e9

int graph[MAX_NODES][MAX_NODES];

int dist[MAX_NODES];

int visited[MAX_NODES];

int main()
{
    int n, start, m;
    scanf("%d%d%d", &n, &start, &m);
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            graph[i][j] = INF;
        }
    }

    for (int i = 0; i < m; i++)
    {
        int u, v, w;
        scanf("%d%d%d", &u, &v, &w);
        graph[u][v] = w;
        graph[v][u] = w;
    }
    for (int i = 1; i <= n; i++)
    {
        if (i == start)
        {
            dist[i] = 0;
        }
        else
        {
            dist[i] = INF;
        }
    }


    int total_cost = 0;
    for (int i = 1; i <= n; i++)
    {
        int min_dist = INF, min_node = -1;
        for (int j = 1; j <= n; j++)
        {
            if (!visited[j] && dist[j] < min_dist)
            {
                min_dist = dist[j];
                min_node = j;
            }
        }
        if (min_node == -1)
        {
            break;
        }
        visited[min_node] = 1;
        total_cost += dist[min_node];
        for (int j = 1; j <= n; j++)
        {
            if (graph[min_node][j] != INF && !visited[j] && graph[min_node][j] < dist[j])
            {
                dist[j] = graph[min_node][j];
            }
        }
    }
    printf("%d\n", total_cost);
    return 0;
}