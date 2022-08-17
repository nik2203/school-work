#include<stdio.h>

int main(){
    int n,r,rem;
    scanf("%d",&n);
    while(rem>0){
        rem=n%10;
        n=n/10;
    }
    return 0;
}