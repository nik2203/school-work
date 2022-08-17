#include<stdio.h>

int bin_search(int N[],int key,int lp, int rp){
    int mid=(lp+(rp-1))/2;
    if(rp>=lp){
        if(N[mid]==key){
            return mid;
        }
        if(N[mid]>key){
            return bin_search(N,key,lp,mid-1);
        }
        if(N[mid]<key){
            return bin_search(N,key,mid+1,rp);
        }
    }
    else{
        return -1;
    }
}

void sort(int N[],int k){
    for(int i=0;i<k;i++){
        for(int j=0;j<k-i-1;j++){
            if(N[j]>N[j+1]){
                int temp=N[j+1];
                N[j+1]=N[j];
                N[j]=temp;
            }
        }
    }
}

int main(){
    int k,i,res;
    scanf("%d",&k);
    int N[k];
    int key;
    for(i=0;i<k;i++){
        scanf("%d",&N[i]);
        printf("%d\n",N[i]);
    }
    scanf("%d",&key);
    sort(N,k);
    int ele=sizeof(N)/sizeof(N[0]);
    res=bin_search(N,key,0,ele);
    
    if(res==-1){
        printf("Not found");
    }
    else{
        printf("Found");
    }
    return 0;
}




