#include <stdlib.h>
#include <math.h>
#include <stdio.h>



int matrixScore(int **grid, int gridSize, int *gridColSize){
    for (int i = 0; i < gridSize; i++){
        if (grid[i][0] == 0){
            for (int j = 0; j < *gridColSize; j++){
                if (grid[i][j] == 1){
                    grid[i][j]--;
                }
                else{
                    grid[i][j]++;
                }
            }
        }
    }
    int colsum = 0;
    for (int j = 1; j < *gridColSize; j++){
        colsum = 0;
        for (int i = 0; i < gridSize; i++){
            colsum += grid[i][j];
        }
        if (colsum < (gridSize - colsum)){
            for (int i = 0; i < gridSize; i++){
                if (grid[i][j] == 1){
                    grid[i][j]--;
                }
                else{
                    grid[i][j]++;
                }
            }
        }
    }

    int sum = 0;
    for (int i = 0; i < gridSize; i++){
        for (int j = 0; j < *gridColSize; j++){
            if (grid[i][j] == 1){
                sum += (int)(pow(2.0, *gridColSize - j - 1));
            }
        }
    }
    return sum;
}


void main(){
    // Driver Code
    int n;
    int m;
    scanf("%d", &n);
    int **mat = (int **)malloc(n * sizeof(int *));
    scanf("%d", &m);
    for (int i = 0; i < n; i++){
        mat[i] = (int *)malloc(m * sizeof(int));
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            scanf("%d", &mat[i][j]);
        }
    }
    printf("%d", matrixScore(mat, n, &m));
}