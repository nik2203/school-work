#include <stdlib.h>
#include <stdio.h>

#define ZERO 0
#define ONE 1

/*edge list structure for each edge */
typedef struct
{
    unsigned int first;
    unsigned int second;
} edge;

unsigned int cyclic_recursive(const edge *edges, unsigned int n, unsigned int *vis,
                              unsigned int order, unsigned int vertex, unsigned int pred);

unsigned int cycle_finder(const edge *edges, unsigned int n, unsigned int order);

/* DO NOTE THAT THE GRAPH TRAVERSAL IN THIS QUESTION ALWAYS STARTS WITH NODE 0  so you need not take any input for starting node */
int main(void)
{
    unsigned int order; /* number of vertices */
    unsigned int n;     /* number of edges */
    scanf("%d", &n);
    scanf("%d", &order);
    edge *edges;
    unsigned int ans;
    edges = malloc(n * sizeof(edge));
    if (edges == NULL)
    {
        return 1;
    }
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &edges[i].first);
        scanf("%d", &edges[i].second);
    }

    ans = cycle_finder(edges, n, order);
    printf("\n");
    printf(ans ? "cyclic" : "acyclic");
    free(edges);
    return 0;
}

unsigned int cyclic_recursive(const edge *edges, unsigned int n, unsigned int *vis,
                              unsigned int order, unsigned int vertex, unsigned int pred)
{
    unsigned int i = ZERO, cycle_found = ZERO;
    vis[vertex] = ONE;
    while (i < n && !cycle_found)
    {
        if (edges[i].first == vertex || edges[i].second == vertex)
        {
            const unsigned int neighbour = edges[i].first == vertex ? edges[i].second : edges[i].first;
            if (vis[neighbour] == ZERO)
            {
                cycle_found = cyclic_recursive(edges, n, vis, order, neighbour, vertex);
            }
            else if (neighbour != pred)
            {
                cycle_found = ONE;
            }
        }
        i++;
    }
    return cycle_found;
}

unsigned int cycle_finder(const edge *edges, unsigned int n, unsigned int order)
{
    unsigned int *vis = calloc(order, sizeof(unsigned int));
    unsigned int cycle_found;
    if (vis == NULL)
    {
        return ZERO;
    }
    cycle_found = cyclic_recursive(edges, n, vis, order, 0, 0);
    free(vis);
    return cycle_found;
}