#include<stdio.h>

/*int f1(int c);

int main(){
    int a;
    a=f1(10);
    printf("%d",a);
    return 0;
}

int f1(int b){
    if(b==0){
        return 0;
    }
    else{
        printf("a");
        f1(--b);
    }
}*/

int main(){
    int a=10;
    int *p;
    p=&a;
    printf("%d",*p);
    return 0;
}