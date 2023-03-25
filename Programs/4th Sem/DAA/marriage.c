#include <stdio.h>

int marriage(int boys[], int girls[], int n)
{
    int temp,res=0;
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(boys[j]>boys[j+1]){
                temp = boys[j];
                boys[j] = boys[j+1];
                boys[j+1] = temp;
            }
        }
    }
    for(int i = 0;i<n;i++){
        if(boys[i]==girls[i]){
            res++;
        }
    }
    return res;
}

// Driver code
int main()
{
    int n;
    scanf("%d", &n);
    int boys[n], girls[n], res;
    for (int i = 0; i < n; i++)
        scanf("%d", &boys[i]);
    for (int i = 0; i < n; i++)
        scanf("%d", &girls[i]);
    res = marriage(boys, girls, n);
    printf("%d", res);
    return 0;
}
