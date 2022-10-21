#include<stdio.h>

#define MAX 50

void top_up(int *h,int n){
    int i, parent, k, key;
    for(k=1;k<=n;k++){
        i=k;
        key=h[i];
        parent=(i-1)/2;
        while((i>0)&&(key>h[parent])){
            h[i]=h[parent];
            i=parent;
            parent=(i-1)/2;
        }
        h[i]=key;
    }
}

int max_heap(int *h, int *n){
    int max;
    max=h[0];
    int temp=h[*n-1];
    h[*n-1]=max;
    h[0]=temp;
    --*n;
    top_up(h,*n);
    return(max);
}

int main(){
    int h[MAX],i,n;
    printf("Enter the No. of Elements\n");
    scanf("%d",&n);
    printf("Enter the elements into array\n");
    for(i=0;i<n;i++){
        scanf("%d",&h[i]);
    }
    printf("Before heapify\n");
    for(i=0;i<n;i++){
        printf("\n%d\t");
    }
}