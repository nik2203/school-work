#include<stdio.h>

int main(){
    int d,m,y,md;
    d=28;
    m=2;
    y=2016;
    if(m==1 || m==3 || m==5 || m==7 || m==8 || m==10 || m==12){
        md=31;
    }
    else if(m==4 || m==6 || m==9 || m==11){
        md=30;
    }
    else if(m==2 &&(y%400==0 || (y%4==0 && y%100!=0))){
        md=29;
    }
    else{
        md=28;
    }
    if (d>=1 && d<md){
        printf("%d-%d-%d",d+1,m,y);
    }
    else if (d==md){
        if(m==12){
            printf("%d-%d-%d",1,1,y+1);
        }
        else{
            printf("%d-%d-%d",1,m+1,y);
        }
    }

    return 0;
}