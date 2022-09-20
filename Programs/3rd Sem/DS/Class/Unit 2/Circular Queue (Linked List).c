#include<stdio.h>
#include<stdlib.h>


//node structure
typedef struct node{
	int data;
	struct node* link;
}NODE;

//circular queue structure with pointers to front and rear nodes
typedef struct cq{
	NODE *f,*r;
}CQ;

//function to add nodes to the queue
void enqueue(CQ *ptr, int ele){
	NODE *temp=malloc(sizeof(NODE));
	temp->data=ele;
	if(ptr->f==NULL){
		ptr->f=ptr->r=temp;
	}
	ptr->r->link=temp;
	temp->link=ptr->f;
	ptr->r=temp;
	printf("Successfully enqueued\n");
}

//function to delete nodes from a queue
int dequeue(CQ *ptr){
    int x;
	if(ptr->f==NULL){ //accounting for empty queue
		return 9999;
	}
	else{
		if(ptr->f==ptr->r){
			x=ptr->f->data;
			free(ptr->f);
			ptr->f=ptr->r=NULL;
			return x;
		}
		NODE *second=ptr->f->link;
		x=ptr->f->data;
	}
}

void display(CQ *ptr){
	if(ptr->f==NULL){
		printf("Underflow condition\n");  //accounting for empty queue
		return;
	}
	NODE *cur=ptr->f;
	while(cur!=ptr->r){
		printf("%d\t",cur->data);
		cur=cur->link;
	}
	printf("%d\n",cur->data);
}

int main(){
	//dynamically allocate memory for circular queue
	CQ *ptr=malloc(sizeof(CQ));
	ptr->f=ptr->r=NULL; //initialise the front and rear node pointers to point to null as queue is empty
	int choice,ele,x;
	while(1){
		printf("Enter your choice\n");
		printf("1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n");
		scanf("%d",&choice);
		switch (choice){
			case 1: printf("Enter the element\n");
					scanf("%d",&ele);
					enqueue(ptr,ele);
					break;
			case 2: x=dequeue(ptr);
					if(x==9999){
						printf("Underflow condition\n");
					}
					else{
						printf("The dequeued element is %d\n",x);
					}
					break;
			case 3: printf("The queue is:\n");
					display(ptr);
					break;
			case 4: exit(0);
		}
	}
	return 0;
}