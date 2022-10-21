#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *rlink;
    struct node *llink;
}NODE;

void insert(NODE *root, int ele){
    NODE *temp=malloc(sizeof(NODE));
    temp->data=ele;
    temp->rlink=temp->llink=NULL;
    if(root==NULL){
        root=temp;
        return;
    }
    NODE *cur=root;
    NODE *prev=NULL;
    while(cur!=NULL){
        prev=cur;
        if(ele<cur->data){
            cur=cur->llink;
        }
        else{
            cur=cur->rlink;
        }
    }
    if(ele<prev->data){
        prev->llink=temp;
    }
    else{
        prev->rlink=temp;
    }
}

void preorder(){
    
}

int main(){
    NODE *root=NULL;
    return 0;
}