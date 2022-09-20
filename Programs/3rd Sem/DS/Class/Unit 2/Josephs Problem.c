#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *link;
}NODE;

void create(NODE **head){
    int n;
    NODE *rear;
    printf("Enter the value of n\n");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        NODE *temp=malloc(sizeof(NODE));
        temp->data=i;
        if((*head)->link==NULL){
            (*head)->link=temp;
        }
        else{
            rear->link=temp;
        }
        rear=temp;
    }
    rear->link=(*head)->link;
}

void display(NODE *head){
    if(head->link==NULL){
        printf("List is empty\n");
    }
    else{
        
    }
}

int main(){
    NODE *ptr=malloc(sizeof(NODE));
    ptr->link=NULL;
    create(&ptr);
    printf("List of people in the circular queue is\n");
    display(ptr);
    return 0;
}