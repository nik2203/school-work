#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int left[], int right[], int left_len, int right_len) {
    int i = 0, j = 0, k = 0;
    while (i < left_len && j < right_len) {
        if (left[i] < right[j]) {
            arr[k] = left[i];
            i++;
        } else if (left[i] > right[j]) {
            arr[k] = right[j];
            j++;
        } else {
            arr[k] = left[i];
            i++;
            j++;
        }
        k++;
    }
    while (i < left_len) {
        arr[k] = left[i];
        i++;
        k++;
    }
    while (j < right_len) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

void merge_sort(int arr[], int n) {
    if (n < 2) {
        return;
    }
    int mid = n / 2;
    int *left = (int*) malloc(mid * sizeof(int));
    int *right = (int*) malloc((n - mid) * sizeof(int));
    for (int i = 0; i < mid; i++) {
        left[i] = arr[i];
    }
    for (int i = mid; i < n; i++) {
        right[i - mid] = arr[i];
    }
    merge_sort(left, mid);
    merge_sort(right, n - mid);
    merge(arr, left, right, mid, n - mid);
    free(left);
    free(right);
}

void solution(int rollnumber[], int n) {
    merge_sort(rollnumber, n);
    for (int i = 0; i < n; i++) {
        printf("%d ", rollnumber[i]);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    solution(arr, n);
    return 0;
}
