#include<stdio.h>
#include<stdlib.h>

typedef struct node{
	struct node* prev;
	struct node* next;
	int data;
}NODE;

/*typedef struct cdll{
	NODE* head;
	int no_node;
}CDLIST;

CDLIST *init(){
	CDLIST *temp=(CDLIST*)malloc(sizeof(CDLIST));
	temp->head=temp;
	temp->no_node=0;
	return temp;
}*/

NODE *create_node(){
	NODE *temp=(NODE*)malloc(sizeof(NODE));
	if(temp!=NULL){
		return temp;
	}
}

void insert_front(NODE *ptr,int ele){
	NODE *temp=create_node();
	temp->data=ele;
	NODE *first=ptr->next;
	ptr->next=temp;
	temp->prev=ptr;
	temp->next=first;
	first->prev=temp;
}

void insert_rear(NODE *ptr,int ele){
	NODE *temp=create_node();
	temp->data=ele;
	NODE *last=ptr->prev;
	ptr->prev=temp;
	temp->next=ptr;
	temp->prev=last;
	last->next=temp;
}

int delete_front(NODE *ptr){
	NODE *temp=ptr->next;
	if(temp==ptr){
		return 9999;
	}
	else{
		NODE *next=ptr->next->next;
		int x=temp->data;
		ptr->next=next;
		next->prev=ptr;
		temp->next=NULL;
		temp->prev=NULL;
		free(temp);
		return x;
	}
}

int delete_rear(NODE *ptr){
	NODE *last=ptr->prev;
	NODE *seclast=last->prev;
	if(ptr->next==ptr){
		return 9999;
	}
	else{
		int x=last->data;
		seclast->next=ptr;
		ptr->prev=seclast;
		last->next=NULL;
		last->prev=NULL;
		free(last);
		return x;
	}
}

void display(NODE *ptr){
	NODE *cur=ptr->next;
	if(cur==ptr){
		printf("The list is empty\n");
		return;
	}
	else{
		printf("The list is:\n");
		while(cur!=ptr){
			printf("%d\t",cur->data);
			cur=cur->next;
		}
	}
	printf("\n");
}

int main(){
	NODE *head=create_node();
	head->next=head;
	head->prev=head;
	int choice,ele,x;
	while(1){
		printf("Enter your choice\n");
		printf("1.Insert at front\n2.Insert at rear\n3.Delete at front\n4.Delete at rear\n5.Display\n6.Exit\n");
		scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter the element to insert\n");
					scanf("%d",&ele);
					insert_front(head,ele);
					break;
			case 2: printf("Enter the element to insert\n");
					scanf("%d",&ele);
					insert_rear(head,ele);
					break;
			case 3: x=delete_front(head);
					if(x==9999){
						printf("The list is empty\n");
					}
					else{
						printf("The deleted element is %d\n",x);
					}
					break;
			case 4: x=delete_rear(head);
					if(x==9999){
						printf("The list is empty\n");
					}
					else{
						printf("The deleted element is %d\n",x);
					}
					break;
			case 5: display(head);
					break;
			case 6: exit(0);
		}
	}
	return 0;
}