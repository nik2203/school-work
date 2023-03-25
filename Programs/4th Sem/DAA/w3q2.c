#include <math.h>
#include <stdio.h>

void find_swaps(int studentline[], int N)
{
    int swaps = 0;
    for (int i = 1; i < N; i++) {
        int key = studentline[i];
        int j = i - 1;
        while (j >= 0 && studentline[j] > key) {
            studentline[j + 1] = studentline[j];
            j--;
            swaps++;
        }
        studentline[j + 1] = key;
    }
    printf("%d\n", swaps);
}

void main()
{
    //Drivers Code
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    find_swaps(arr, n);
}
