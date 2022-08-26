#include<stdio.h>
#include<stdlib.h>


typedef struct node{
	int data;
	struct node* link;
}NODE;

/*typedef struct cslist{
	NODE *head;
}CSLIST;

CSLIST *init(){
	CSLIST *temp=(CSLIST*)malloc(sizeof(CSLIST));
	if(temp!=NULL){
		temp->head=NULL;
		return(temp);
	}
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
	NODE *first=ptr->link;
	ptr->link=temp;
	temp->link=first;
}

void insert_rear(NODE *ptr,int ele){
	NODE *temp=create_node();
	temp->data=ele;
	NODE *cur=ptr->link;
	while(cur->link!=ptr){
		cur=cur->link;
	}
	cur->link=temp;
	temp->link=ptr;
}

int delete_front(NODE *ptr){
	NODE *temp=ptr->link;
	if(temp==ptr){
		return 9999;
	}
	else{
		int x=temp->data;
		ptr->link=temp->link;
		temp->link=NULL;
		free(temp);
		return x;
	}
}

int delete_rear(NODE *ptr){
	NODE *cur=ptr->link;
	NODE *next=cur->link;
	if(cur==ptr){
		return 9999;
	}
	else{
		while(next->link!=ptr){
			cur=cur->link;
			next=next->link;
		}
		int x=next->data;
		cur->link=ptr;
		next->link=NULL;
		free(next);
		return x;
	}
}


void display(NODE *ptr){
	NODE *cur=ptr->link;
	if(cur==ptr){
		printf("The list is empty\n");
		return;
	}
	else{
		printf("The list is:\n");
		while(cur!=ptr){
			printf("%d\t",cur->data);
			cur=cur->link;
		}
	}
	printf("\n");
}

int main(){
	NODE *head=create_node();
	head->link=head;
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
