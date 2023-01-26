#include <stdio.h>

void getMatrixElements(int matrix[][10], int row, int column)
{
    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < column; ++j)
        {
            scanf("%d", &matrix[i][j]);
        }
    }
}

void multiplyMatrices(int first[][10], int second[][10], int result[][10], int r1, int c1)
{

    int r2 = c1;
    int c2 = r1;
    // Creating a transpose of the matrix:
    for (int i = 0; i < r2; ++i)
    {
        for (int j = 0; j < c2; ++j)
        {
            second[i][j] = first[j][i];
        }
    }

    // Initializing elements of resultant matrix to 0.
    for (int i = 0; i < r1; ++i){
        for (int j = 0; j < c2; ++j)
        {
            result[i][j] = 0;
        }
    }

    // Multiplying  matrices and storing it in result
    for (int i = 0; i < r1; ++i){
        for (int j = 0; j < c2; ++j)
        {
            for (int k = 0; k < c1; ++k)
            {
                result[i][j] += first[i][k] * second[k][j];
            }
        }
    }
}

// Driver Code

int main()
{
    int i, j, r1, c1;
    scanf("%d %d", &r1, &c1);
    int A[10][10], B[10][10], result[10][10];
    getMatrixElements(A, r1, c1);
    multiplyMatrices(A, B, result, r1, c1);
    printf("Output -\n");
    for (i = 0; i < r1; i++)
    {
        for (j = 0; j < r1; j++)
            printf("%d\t", result[i][j]);
        printf("\n");
    }
    return 0;
}