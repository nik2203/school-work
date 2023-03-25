#include <stdio.h>

int partition(int array[], int low, int high) {
    int pivot = array[low], i = low - 1, j = high + 1;
    while (1) {
        do {
            i++;
        } while (array[i] < pivot);
        do {
            j--;
        } while (array[j] > pivot);
        if (i >= j) {
            return j;
        }
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

void carsequence(int array[], int low, int high) {
    if (low < high) {
        int pi = partition(array, low, high);
        carsequence(array, low, pi);
        carsequence(array, pi + 1, high);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    carsequence(arr, 0, n - 1);
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}
