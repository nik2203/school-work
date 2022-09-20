#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#define MAX 5

typedef struct qnode{
	int data;
	struct qnode *link;
}NODE;

typedef struct queue{
	NODE * front, *rear;
}QUEUE;

QUEUE * createQueue(){
	QUEUE *temp=malloc(sizeof(QUEUE));
	temp->front=temp->rear=NULL;
}

void enqueue(QUEUE *ptr,int ele){
	NODE *temp=malloc(sizeof(NODE));
	temp->data=ele;
	temp->link=NULL;
	if(ptr->rear==NULL){
		ptr->front=ptr->rear=temp;
		return;
	}
	ptr->rear->link=temp;
	ptr->rear=temp;
}

int dequeue(QUEUE *ptr){
	if(ptr->front==NULL && ptr->rear==NULL){
		return 9999;
	}
	else if(ptr->front==ptr->rear){
		NODE *first=ptr->front;
		int x=first->data;
		free(first);
		ptr->front=ptr->rear=NULL;
		return(x);
	}
	NODE *first=ptr->front;
	ptr->front=first->link;
	int x=first->data;
	free(first);
	return(x);
}

void display(QUEUE *ptr){
	if(ptr->front==NULL && ptr->rear==NULL){
		printf("Queue is Empty\n");
	}
	else{
		for(NODE *temp=ptr->front;temp!=NULL;temp=temp->link){
			printf("%d\t",temp->data);
		}
	}
	printf("\n");
}

int main(){
	int choice,x;
	QUEUE *q=createQueue();
	while(1){
		printf("1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n");
		printf("Enter the choice\n");
		scanf("%d",&choice);
		switch (choice){
		case 1: printf("Enter element to enqueue\n");
				scanf("%d",&x);
				enqueue(q,x);
				break;
		case 2: x=dequeue(q);
				if(x==9999){
					printf("The queue is empty\n");
				}
				else{
					printf("Dequeued element is %d\n",x);
				}
				break;
		case 3: printf("The queue is:\n");
				display(q);
				break;
		case 4: exit(0);
		}
	}
	return 0;
}








void enque(){
}

int dequeue(){
	
}

int main(){
	int q[MAX],f=0,r=-1;
	int choice,ele; 
	while(1){
		printf("1.Enque\n2.Deque\n3.Display\n4.Exit\n");
		printf("Enter your choice\n");
		scanf("%d",&choice);
		switch(choice){

		}
	}
}

typedef struct stack{
	char arr[MAX];
	int top;
}STACK;

void push(STACK *ptr, char ele){
	ptr->top++;
	ptr->arr[ptr->top]=ele;
}

void pop(STACK *ptr){
	ptr->top--;
}
